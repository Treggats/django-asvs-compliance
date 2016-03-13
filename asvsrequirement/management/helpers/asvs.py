# -*- encoding: utf-8 -*-
import json
from codecs import open
from django.shortcuts import get_object_or_404

from asvs.settings import ASVS_VERSION, ASVS_RELEASE_DATE
from asvsrequirement.models import AsvsVersion, Level, Category, Requirement


class ASVS(object):
    def __init__(self, file, version=ASVS_VERSION,
                 release_date=ASVS_RELEASE_DATE):
        self._version = version
        self._release_date = release_date
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def load_version(self):
        AsvsVersion.objects.get_or_create(version_number=self._version,
                                          release_date=self._release_date)

    def load_level(self):
        for level_nr in sorted(self.reader.get('level')):
            item = self.reader.get('level').get(level_nr)
            lang_code = list(item)[0]
            name = item[lang_code]
            level = Level.objects.language(lang_code).create(
                level_number=level_nr,
                name=name,
                version=get_object_or_404(AsvsVersion,
                                          version_number=self._version)
            )
            level.save()

    def load_category(self):
        for cat_nr in sorted(self.reader.get('category')):
            item = self.reader.get('category').get(cat_nr)
            lang_code = list(item)[0]
            title = item[lang_code]
            category = Category.objects.language(lang_code).create(
                category_number=cat_nr,
                name=title,
                version=get_object_or_404(AsvsVersion,
                                          version_number=self._version)
            )
            category.save()

    def load_requirement(self):
        for req_nr in sorted(self.reader.get('requirement')):
            item = self.reader.get('requirement').get(req_nr)
            lang_code = list(item.get('title'))[0]
            title = item.get('title').get(lang_code)
            cat_nr = item.get('category_nr')
            level_numbers = item.get('levels')

            requirement = Requirement.objects.language(lang_code).create(
                pk=req_nr,
                requirement_number=item.get('requirement_nr'),
                title=title,
                category=Category.objects.language(lang_code)
                                 .get(category_number=cat_nr),
            )
            requirement.save()
            levels = Level.objects.language(lang_code).filter(
                level_number__in=level_numbers)
            requirement.levels = levels
            requirement.save()
