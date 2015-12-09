#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from codecs import open
from pathlib import Path

from asvs.settings import LANGUAGE_CODE
# from asvsannotation.models import AnnotationRelation, AnnotationRequirement,\
#     AnnotationExplanation, AnnotationExplanationType
from asvsrequirement.models import Requirement, Category


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
        src_path = Path(str(src_path)).resolve()
        requirements = Requirement.objects.language(LANGUAGE_CODE).all()
        categories = Category.objects.language(LANGUAGE_CODE).all()

        for category in categories:
            for requirement in requirements.filter(category=category):
                print(category)
                print(requirement)

'''
    def load_requirement(self):
        for pk, value in enumerate(self.reader.get('requirements'), start=1):
            lang_code = list(value.get('shortTitle'))[0]
            req_nr = int(value.get('nr'))
            cat_nr = int(value.get('chapterNr'))
            title = value.get('shortTitle').get(lang_code)

            req = Requirement.objects.language(lang_code).filter(
                category__category_number=cat_nr).filter(
                requirement_number=req_nr)

            if req:
                AnnotationRequirement.objects.language(lang_code)\
                    .get_or_create(
                        pk=pk,
                        requirement=req[0],
                        category=Category.objects.language(lang_code).get(
                            category_number=cat_nr),
                        title=title
                )

                for item in value.get('related'):
                    AnnotationRelation.objects.language(
                        lang_code).get_or_create(
                        req_annotate_pk=pk,
                        name=item.get('name'),
                        url=item.get('url')
                    )

                requirement = AnnotationRequirement.objects.language(
                    lang_code).get(pk=pk)

                for item in value.get('related'):
                    related_items = AnnotationRelation.objects.language(
                        lang_code).filter(req_annotate_pk=pk)

                    requirement.relations = related_items
                    requirement.save()

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
