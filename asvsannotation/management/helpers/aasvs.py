#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import json
from codecs import open
from pathlib import Path

from asvs.settings import LANGUAGE_CODE
# from asvsannotation.models import AnnotationRelation, AnnotationRequirement,\
#     AnnotationExplanation, AnnotationExplanationType
from asvsrequirement.models import Requirement, Category
from asvsannotation.models import AnnotationType


class AASVS(object):
    def __init__(self, file=None):
        self.file = file
        if file is not None:
            self.json_file = open(file, encoding='utf-8')
            self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        if self.file:
            self.json_file.close()

    def process_data(self, src_path):
        src_path = str(Path(str(src_path)).resolve())
        requirements = Requirement.objects.language(LANGUAGE_CODE).all()
        categories = Category.objects.language(LANGUAGE_CODE).all()
        type_list = list()
        for (path, dirs, files) in os.walk(src_path + '/help/'):
            for filename in files:
                file_info = filename.split('.')
                if file_info[-1] == 'md' and file_info[0] not in type_list:
                    type_list.append(file_info[0])
        
        for type_item in type_list:
            item = AnnotationType.objects.language(LANGUAGE_CODE).get_or_create(
                title=type_item
            )

        help_dir = src_path + '/help/'

        for category in categories:
            for requirement in requirements.filter(category=category):
                if os.path.isdir("{}{}".format(
                    help_dir,
                    category.category_number
                )):
                    print("correct")
                else:
                    print("not so correct")


'''
    def load_help_text(self, path):
        path = Path(str(path)).resolve()
        requirements = Requirement.objects.language(LANGUAGE_CODE).all()
        annotations = AnnotationRequirement.objects.all()

        for requirement in requirements:
            req_nr = requirement.requirement_number
            cat_nr = requirement.category_version
            if os.path.isdir("{}/{}/{}/en".format(path, cat_nr, req_nr)):
                annotation = annotations.filter(
                    category__category_number__exact=cat_nr).filter(
                    requirement__requirement_number__exact=req_nr)

                annotationtypes = AnnotationExplanationType.objects.language(
                    LANGUAGE_CODE).all()
                for type in annotationtypes:
                    file = "{}/{}/{}/en/{}.md".format(path, cat_nr, req_nr,
                                                      type)
                    if os.path.exists(file):
                        with open(file) as f:
                            explanation = AnnotationExplanation.objects.language(
                                LANGUAGE_CODE).get_or_create(
                                req_ann=annotation[0],
                                type=AnnotationExplanationType.objects.language(
                                    LANGUAGE_CODE).get(pk=type.pk),
                                explanation=f.read()
                            )
        return "Done"
'''
