# -*- encoding: utf-8 -*-
import json
from codecs import open


class ASVS(object):
    def __init__(self, file):
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def __str__(self):
        str = ""
        str = self.create_version_fixture()
        str = self.create_category_name_fixture()
        return str

    def create_version_fixture(self, versions=(3,)):
        """
        [
            {
                "fields": {
                    "version": "3"
                },
                "model": "level.version",
                "pk": 1
            }
        ]
        :param versions: a list with versions
        :return: a Django fixture representation of ASVS Version
        """
        fixture = list()
        for pk, version in enumerate(versions):
            part = dict(fields=dict(version=version),
                        model='level.version',
                        pk=pk + 1)
            fixture.append(part)
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_category_name_fixture(self):
        """
        [
            {
                "fields": {
                    "category_number": 1,
                    "lang_code": "en",
                    "name": "Architecture, design and threat modelling"
                },
                "model": "level.categoryname",
                "pk": 1
            }
        ]
        :return: a Django fixture representation of Category Name
        """
        fixture = list()
        for pk, nr in enumerate(self.reader.get('chapters')):
            category = self.reader.get('chapters').get(nr)
            lang_code = list(category.get('name').keys())[0]
            cat_name = category.get('name').get(lang_code)
            part = dict(fields=dict(category_number=int(nr),
                                    lang_code=lang_code,
                                    name=cat_name, ),
                        model='level.categoryname',
                        pk=pk + 1)
            fixture.append(part)
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))
