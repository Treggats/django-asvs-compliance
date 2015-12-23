#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
import json
from codecs import open
from pathlib import Path
from django.shortcuts import get_object_or_404

from asvs.settings import LANGUAGE_CODE
from asvsrequirement.models import Requirement, Category
from asvsannotation.models import AnnotationType, AnnotationHelp, Annotation


class AASVS(object):
    def __init__(self, src_path):
        self.requirement_object = Requirement.objects.language(LANGUAGE_CODE)
        self.category_object = Category.objects.language(LANGUAGE_CODE)
        self.annotation_type_object = AnnotationType.objects.language(LANGUAGE_CODE)
        self.annotation_help_object = AnnotationHelp.objects.language(LANGUAGE_CODE)
        self.annotation_object = Annotation.objects.language(LANGUAGE_CODE)

        self.src_path = str(Path(str(src_path)).resolve())

    def process_types(self):
        help_dir = self.src_path + '/help/'
        for (path, dirs, files) in os.walk(help_dir):
            for filename in files:
                file_info = filename.split('.')
                self.annotation_type_object.get_or_create(title=file_info[0])

    def process_help(self):
        help_dir = self.src_path + '/help/'
        for (path, dirs, files) in os.walk(help_dir):
            for filename in files:
                file_info = filename.split('.')
                annotation_type = self.annotation_type_object.get(title=file_info[0])
                cat_nr = path.split('/')[-3]
                req_nr = path.split('/')[-2]
                cat = self.category_object.get(category_number=cat_nr)
                try:
                    req = self.requirement_object.get(category=cat,
                                                 requirement_number=req_nr)
                    with open("{}/{}".format(path, filename)) as f:
                        self.annotation_help_object.get_or_create(annotation_type=annotation_type,
                            requirement=req,
                            help_text=f.read())
                except:
                    print("[Annotation Help] Requirement: {}, Category: {} does not exist".format(req_nr, cat_nr))

    def process_data(self, src_path):        
        help_dir = src_path + '/help/'

        
        json_file = open(src_path + '/aasvs.json', encoding='utf-8')
        reader = json.load(json_file)

        for item in reader.get('requirements'):
            cat_nr = item.get('chapterNr')
            req_nr = item.get('nr')
            short_title = item.get('shortTitle')['en']

            try:
                cat = category_object.get(category_number=cat_nr)
            except:
                error = sys.exc_info()
                print(error)
            try:
                req = requirement_object.get(category=cat,
                                             requirement_number=req_nr)
            except:
                error = sys.exc_info()
                print(error)
                print("[] Requirement: {}, Category: {} does not exist\n".format(req_nr, cat_nr))

                try:
                    ann_help = annotation_help_object.filter(requirement=req,category=cat)
                except:
                    error = sys.exc_info()
                    print(error)

            try:
                annotation_object.get_or_create(requirement=req,
                                                category=cat,
                                                # annotation_help=ann_help,
                                                title=short_title)
            except:
                error = sys.exc_info()
                print(error)
            # except:
            #     print("Requirement: {}, Category: {} does not exist".format(req_nr, cat_nr))
