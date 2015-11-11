# -*- encoding: utf-8 -*-
import json
from codecs import open


class ASVS(object):
    def __init__(self, file):
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)
        self.global_fixture = dict()

        """Process all the models"""
        self.create_version_fixture()
        self.create_level_fixture()
        self.create_category_fixture()
        self.create_requirement_fixture()

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def get_json(self, fixture):
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def get(self, model):
        if model == 'version':
            return self.get_json(self.global_fixture.get('version'))
        elif model == 'level':
            return self.get_json(self.global_fixture.get('level'))
        elif model == 'category':
            return self.get_json(self.global_fixture.get('category'))
        elif model == 'requirement':
            return self.get_json(self.global_fixture.get('requirement'))
        elif model == 'all':
            output = list()
            for item in self.global_fixture.get('version'):
                output.append(item)
            for item in self.global_fixture.get('level'):
                output.append(item)
            for item in self.global_fixture.get('category'):
                output.append(item)
            for item in self.global_fixture.get('requirement'):
                output.append(item)
            return self.get_json(output)
        else:
            """TODO: Change back to None"""
            return self.get_json(self.global_fixture)

    def _get_version_pk(self, version='3'):
        """
        Get the primary key for AsvsVersion
        :param version: The ASVS version, defaults to 3
        :return: The primary key
        """
        for item in self.global_fixture.get('version'):
            if item.get('fields').get('version_number') == int(version):
                return item.get('pk')
        return None

    def _get_category_pk(self, cat_nr):
        """
        Get the primary key for Category
        :param cat_nr: The number of a Category
        :return: The primary key
        """
        for item in self.global_fixture.get('category'):
            if item.get('fields').get('category_number') == cat_nr:
                return item.get('pk')
        return None

    def create_version_fixture(self, versions=(3,)):
        """
        [
            {
                "fields": {
                    "version_number": "3"
                },
                "model": "level.asvsversion",
                "pk": 1
            }
        ]
        :param versions: a list with versions
        :return: a Django fixture representation of ASVS Version
        """
        fixture = list()
        for pk, version in enumerate(versions, start=1):
            part = dict(fields=dict(version_number=version),
                        model='level.asvsversion',
                        pk=pk)
            fixture.append(part)
        self.global_fixture.update({'version': fixture})
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_category_fixture(self):
        """
        [
            {
                "fields": {
                    "category_number": 1,
                    "version": 1
                },
                "model": "level.category",
                "pk": 5
            },
            {
                "fields": {
                    "language_code": "en-us",
                    "master": 5,
                    "name": "Architecture, design and threat modelling"
                },
                "model": "level.categorytranslation",
                "pk": 5
            }
        ]
        :return:a Django fixture representation of Category
        """
        fixture = list()
        pk = 1
        for cat_nr in sorted(self.reader.get('category')):
            item = self.reader.get('category').get(cat_nr)
            lang_code = list(item)[0]
            title = item[lang_code]
            part = dict(
                fields=dict(category_number=cat_nr,
                            version=self._get_version_pk()),
                model='level.category', pk=pk)
            trans_part = dict(
                fields=dict(language_code=lang_code,
                            master=pk,
                            name=title),
                model="level.categorytranslation",
                pk=pk
            )
            fixture.append(part)
            fixture.append(trans_part)
            pk += 1
        self.global_fixture.update({'category': fixture})
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_level_fixture(self):
        """
        [
            {
                "fields": {
                    "level_number": 1,
                    "version": 1
                },
                "model": "level.level",
                "pk": 7
            },
            {
                "fields": {
                    "language_code": "en-us",
                    "master": 7,
                    "name": "Opportunistic"
                },
                "model": "level.leveltranslation",
                "pk": 7
            }
        ]
        :return:
        """
        fixture = list()
        pk = 1
        for level_nr in sorted(self.reader.get('level')):
            item = self.reader.get('level').get(level_nr)
            lang_code = list(item)[0]
            name = item[lang_code]
            part = dict(
                fields=dict(level_number=level_nr,
                                    version=self._get_version_pk()),
                        model='level.level',
                        pk=pk)
            trans_part = dict(
                fields=dict(
                    language_code=lang_code,
                    master=pk,
                    name=name),
                model="level.leveltranslation",
                pk=pk)
            fixture.append(part)
            fixture.append(trans_part)
            pk += 1
        self.global_fixture.update({'level': fixture})
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def create_requirement_fixture(self):
        """
        [
            {
                "fields": {
                    "category": 5,
                    "level": [
                        7,
                        8,
                        9
                    ],
                    "requirement_number": 1
                },
                "model": "level.requirement",
                "pk": 1
            },
            {
                "fields": {
                    "language_code": "en-us",
                    "master": 1,
                    "title": "Verify that all application components are identified and are known to be needed."
                },
                "model": "level.requirementtranslation",
                "pk": 1
            }
        ]
        :return: a Django fixture representation for Requirement
        """
        fixture = list()
        pk = 1
        for req_nr in sorted(self.reader.get('requirement')):
            item = self.reader.get('requirement').get(req_nr)
            lang_code = list(item.get('title'))[0]
            title = item.get('title').get(lang_code)
            levels = item.get('levels')
            cat_nr = item.get('category_nr')

            part = dict(
                fields=dict(
                    category=self._get_category_pk(cat_nr),
                    requirement_number=item.get('requirement_nr'),
                    level=levels),
                model='level.requirement',
                pk=pk)
            trans_part = dict(
                fields=dict(
                    language_code=lang_code,
                    master=pk,
                    title=title),
                model="level.requirementtranslation",
                pk=pk
            )
            fixture.append(part)
            fixture.append(trans_part)
            pk += 1
        self.global_fixture.update({'requirement': fixture})
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))
