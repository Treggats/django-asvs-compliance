# -*- encoding: utf-8 -*-
import json
from codecs import open


class ASVS(object):
    def __init__(self, file):
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)
        self.levelnames = list()
        self.categorynames = list()
        self.requirementnames = list()
        self.versions = list()

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def __str__(self):
        str = None
        str = self.create_version_fixture()
        str = self.create_category_name_fixture()
        str = self.create_category_fixture()
        str = self.create_level_name_fixture()
        str = self.create_level_fixture()
        str = self.create_requirement_name_fixture()
        str = self.create_requirement_fixture()
        return str

    def _get_category_name_pk(self, name):
        """
        Get the primary key for category names
        :param name: search for this string
        :return: the primary key
        """
        for item in self.categorynames:
            if item.get('name') == name:
                return item.get('pk')
        return None

    def _get_version_pk(self, version='3'):
        """
        Get the primary key for AsvsVersion
        :param version: the ASVS version, defaults to 3
        :return: the primary key
        """
        for item in self.versions:
            if item.get('version') == int(version):
                return item.get('pk')
        return None

    def _get_level_name_pk(self, level):
        """
        Get the primary key for a certain level
        :param level: a numeric level
        :return: the primary key
        """
        for item in self.levelnames:
            if item.get('number') == level:
                return item.get('pk')
        return None

    def _get_requirement_name_pk(self, req_nr):
        """
        Get the primary key for a certain requirement name
        :param req_nr: a numeric requirement number
        :return: the primary key
        """
        for item in self.requirementnames:
            if item.get('number') == req_nr:
                return item.get('pk')
        return None

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
            self.versions.append(dict(pk=part.get('pk'), version=part.get(
                'fields').get('version')))
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
            lang_code = list(category.get('name').keys())
            cat_name = category.get('name').get(lang_code[0])
            part = dict(fields=dict(category_number=int(nr),
                                    lang_code=lang_code[0],
                                    name=cat_name, ),
                        model='level.categoryname',
                        pk=pk + 1)
            fixture.append(part)
            self.categorynames.append(dict(pk=part.get('pk'),
                                           name=part.get('fields').get('name')))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_category_fixture(self):
        """
        [
            {
                "fields": {
                    "name": 3,
                    "number": 1,
                    "version": 1
                },
                "model": "level.category",
                "pk": 1
            }
        ]
        :return:a Django fixture representation of Category
        """
        fixture = list()
        for pk, nr in enumerate(self.reader.get('chapters')):
            category = list(self.reader.get('chapters').get(nr).get(
                'name').values())
            part = dict(fields=dict(name=self._get_category_name_pk(category[0]),
                                    number=nr,
                                    version=self._get_version_pk()),
                        model='level.category', pk=pk + 1)
            fixture.append(part)
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_level_name_fixture(self):
        """
        [
            {
                "fields": {
                    "lang_code": "en",
                    "level_number": 1,
                    "name": "Opportunistic"
                },
                "model": "level.levelname",
                "pk": 1
            }
        ]
        :return: a Django fixture representation of LevelName
        """
        fixture = list()
        for pk, nr in enumerate(self.reader.get('levelNames')):
            lang_code = list(self.reader.get('levelNames').get(nr))
            name = self.reader.get('levelNames').get(nr).get(lang_code[0])
            part = dict(fields=dict(lang_code=lang_code[0],
                                    level_number=nr,
                                    name=name),
                        model='level.levelname',
                        pk=pk + 1)
            fixture.append(part)
            self.levelnames.append(dict(pk=part.get('pk'),
                                        number=part.get('fields').get(
                                            'level_number')))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_level_fixture(self):
        """
        [
            {
                "fields": {
                    "name": 1,
                    "number": 1,
                    "version": 1
                },
                "model": "level.level",
                "pk": 1
            }
        ]
        :return:
        """
        fixture = list()
        for pk, nr in enumerate(self.reader.get('levelNames')):
            part = dict(fields=dict(name=self._get_level_name_pk(nr),
                                    number=nr,
                                    version=self._get_version_pk()),
                        model='level.level',
                        pk=pk + 1)
            fixture.append(part)
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_requirement_name_fixture(self):
        """
        [
            {
                "fields": {
                    "lang_code": "en",
                    "requirement_number": 1,
                    "title": "Verify that all application components are identified and are known to be needed."
                },
                "model": "level.requirementname",
                "pk": 1
            }
        ]
        :return: a Django fixture representation for RequirementName
        """
        fixture = list()
        for pk, item in enumerate(self.reader.get('requirements')):
            lang_code = list(item.get('title').keys())
            part = dict(fields=dict(lang_code=lang_code[0],
                                    requirement_number=item.get('nr'),
                                    title=item.get('title').get(lang_code[0])),
                        model='level.requirementname',
                        pk=pk + 1)
            fixture.append(part)
            self.requirementnames.append(dict(pk=part.get('pk'),
                                              number=part.get('fields').get(
                                                  'requirement_number')))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_requirement_fixture(self):
        """
        [
            {
                "fields": {
                    "category": 19,
                    "name": 1,
                    "number": 1,
                    "version": 1
                },
                "model": "level.requirement",
                "pk": 1
            }
        ]
        :return: a Django fixture representation for Requirement
        """
        fixture = list()
        for pk, item in enumerate(self.reader.get('requirements')):
            part = dict(fields=dict(category=19,
                                    name=self._get_requirement_name_pk(
                                        item.get('nr')),
                                    number=item.get('nr'),
                                    version=self._get_version_pk()),
                        model='level.requirement',
                        pk=pk + 1)
            fixture.append(part)
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))
