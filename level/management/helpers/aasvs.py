#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from codecs import open
from level.models import RelatedAnnotated, RequirementAnnotated
from level.models import Requirement, Category


class AASVS(object):
    def __init__(self, file):
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def load_requirement(self):
        for pk, value in enumerate(self.reader.get('requirements'), start=1):
            lang_code = list(value.get('shortTitle'))[0]
            req_nr = int(value.get('nr'))
            cat_nr = int(value.get('chapterNr'))
            title = value.get('shortTitle').get(lang_code)

            for item in value.get('related'):
                related = RelatedAnnotated.objects.language(
                    lang_code).get_or_create(
                    name=item.get('name'),
                    url=item.get('url')
                )

            req = Requirement.objects.language(lang_code).filter(
                category__category_number=cat_nr).filter(
                requirement_number=req_nr)

            if req:
                requirement = RequirementAnnotated.objects.language(lang_code)\
                    .get_or_create(
                        pk=pk,
                        requirement=req[0],
                        category=Category.objects.language(lang_code).get(
                            category_number=cat_nr),
                        title=title
                )

                for item in value.get('related'):
                    related_items = RelatedAnnotated.objects.language(
                        lang_code).filter(name__exact=item.get('name'))
                    print(requirement)
                    break
                    # requirement.relations = related_items
                    # requirement.save()
