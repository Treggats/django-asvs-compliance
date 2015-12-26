#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
import json
from codecs import open
from pathlib import Path

from asvs.settings import LANGUAGE_CODE as lang_code
from asvsrequirement.models import Requirement, Category
from asvsannotation.models import AnnotationType,\
    AnnotationHelp, AnnotationRelation, Annotation


class AASVS(object):
    def __init__(self, src_path):
        self.req_obj = Requirement.objects.language(lang_code)
        self.category_object = Category.objects.language(lang_code)
        self.ann_type_object = AnnotationType.objects.language(lang_code)
        self.ann_help_obj = AnnotationHelp.objects.language(lang_code)
        self.ann_relation_obj = AnnotationRelation.objects.language(lang_code)
        self.ann_obj = Annotation.objects.language(lang_code)

        self.src_path = str(Path(str(src_path)).resolve())
        self.json_file = open(self.src_path + '/aasvs.json', encoding='utf-8')
        self.reader = json.load(self.json_file)

    def process_types(self):
        help_dir = self.src_path + '/help/'
        for (path, dirs, files) in os.walk(help_dir):
            for filename in files:
                file_info = filename.split('.')
                self.ann_type_object.get_or_create(title=file_info[0])

    def process_help_items(self):
        help_dir = self.src_path + '/help/'
        for (path, dirs, files) in os.walk(help_dir):
            for filename in files:
                file_info = filename.split('.')
                ann_type = self.ann_type_object.get(title=file_info[0])
                cat_nr = path.split('/')[-3]
                req_nr = path.split('/')[-2]
                cat = self.category_object.get(category_number=cat_nr)
                try:
                    req = self.req_obj.get(category=cat,
                                           requirement_number=req_nr)
                    with open("{}/{}".format(path, filename)) as f:
                        self.ann_help_obj.get_or_create(ann_type=ann_type, requirement=req, help_text=f.read())
                except:
                    print("[Annotation Help] Requirement: {}, Category: {} does not exist".format(req_nr, cat_nr))

    def process_relations(self):
        for item in self.reader.get('requirements'):
            if item.get('related'):
                for related in item.get('related'):
                    try:
                        self.ann_relation_obj.get_or_create(relation_title=related.get('name'), url=related.get('url'))
                    except:
                        print("[Annotation Relation] Could not create relation item")

    def process_annotations(self):
        for item in self.reader.get('requirements'):
            cat_nr = item.get('chapterNr')
            req_nr = item.get('nr')
            short_title = item.get('shortTitle')['en']

            try:
                req = self.req_obj.get(requirement_number=req_nr,
                                       category__category_number=cat_nr)
            except:
                print("[Annotation] Requirement: {}, Category: {} does not exist".format(req_nr, cat_nr))
            try:
                self.ann_obj.get_or_create(requirement=req,
                                           title=short_title)
            except:
                pass
                print("[Annotation] Annotation could not be created")
                if not req:
                    print("\tno Requirement could be found")

            '''load help texts'''
            try:
                ann = self.ann_obj.get(title=short_title)
                help_items = self.ann_help_obj.filter(requirement=req)
                if help_items:
                    ann.annotation_help.add(help_items)
                    ann.save()
            except:
                print("[Annotation] help texts could not be loaded")
                # print(sys.exc_info())
            '''load related items'''
            try:
                ann = self.ann_obj.get(title=short_title)
                related_items = item.get('related')
                if related_items:
                    for related in related_items:
                        rel = self.ann_relation_obj.get(url=related.get('url'))
                        ann.relations.add(rel)
                        ann.save()
            except:
                print("[Annotation] relations could not be loaded")

    def process_data(self):
        pass
