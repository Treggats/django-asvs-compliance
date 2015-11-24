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

    def get_requirement_by_number(self, req_nr, cat_nr):
        nr = 1
        requirement = Requirement.objects.language()\
            .filter(category__category_number=cat_nr)
        for req in requirement:
            if int(req_nr) == nr:
                return req
            nr += 1

    def load_requirement(self):
        for pk, value in enumerate(self.reader.get('requirements'), start=1):
            # print( json.dumps(value, indent=4) )
            lang_code = list(value.get('shortTitle'))[0]
            req_nr = value.get('nr')
            cat_nr = value.get('chapterNr')
            title = value.get('shortTitle').get(lang_code)

            # for item in value.get('related'):
            #     related = RelatedAnnotated.objects.language(lang_code).create(
            #         name=item.get('name'),
            #         url=item.get('url')
            #     )
            #     related.save()
            print(value.get('nr'))
            r = Requirement.objects.language().filter(
                category__category_number=cat_nr).get(
                requirement_number=int(value.get('nr')))

            requirement = RequirementAnnotated.objects.language(lang_code)\
                .get_or_create(
                    pk=pk,
                    requirement=r,
                    category=Category.objects.language(lang_code).get(
                        category_number=cat_nr),
                    title=title
            )
            print(requirement)
            # requirement.save()
            print(self.get_requirement_by_number(req_nr, cat_nr))
            print(title)
            print()

            # for item in value.get('related'):
            #     related_items = RelatedAnnotated.objects.language(
            #         lang_code).filter(name__exact=item.get('name'))
            #     requirement.related = related_items
            #     requirement.save()
