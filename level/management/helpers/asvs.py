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
        self.create_level_name_fixture()
        self.create_level_fixture()
        self.create_category_name_fixture()
        self.create_category_fixture()
        self.create_requirement_name_fixture()
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
        elif model == 'levelname':
            return self.get_json(self.global_fixture.get('levelname'))
        elif model == 'level':
            return self.get_json(self.global_fixture.get('level'))
        elif model == 'categoryname':
            return self.get_json(self.global_fixture.get('categoryname'))
        elif model == 'category':
            return self.get_json(self.global_fixture.get('category'))
        elif model == 'requirementname':
            return self.get_json(self.global_fixture.get('requirementname'))
        elif model == 'requirement':
            return self.get_json(self.global_fixture.get('requirement'))
        elif model == 'all':
            output = list()
            for item in self.global_fixture.get('version'):
                output.append(item)
            for item in self.global_fixture.get('levelname'):
                output.append(item)
            for item in self.global_fixture.get('level'):
                output.append(item)
            for item in self.global_fixture.get('categoryname'):
                output.append(item)
            for item in self.global_fixture.get('category'):
                output.append(item)
            for item in self.global_fixture.get('requirementname'):
                output.append(item)
            for item in self.global_fixture.get('requirement'):
                output.append(item)
            return self.get_json(output)
        else:
            return None

    def _get_category_name_pk(self, nr):
        """
        Get the primary key for category names
        :param nr: numeric number
        :return: the primary key
        """
        for item in self.global_fixture.get('categoryname'):
            if item.get('fields').get('category_number') == int(nr):
                return item.get('pk')
        return None

    def _get_version_pk(self, version='3'):
        """
        Get the primary key for AsvsVersion
        :param version: the ASVS version, defaults to 3
        :return: the primary key
        """
        for item in self.global_fixture.get('version'):
            if item.get('fields').get('version_number') == int(version):
                return item.get('pk')
        return None

    def _get_level_name_pk(self, level):
        """
        Get the primary key for a certain level
        :param level: a numeric level
        :return: the primary key
        """
        for item in self.global_fixture.get('levelname'):
            if item.get('fields').get('level_number') == level:
                return item.get('pk')
        return None

    def _get_requirement_name_pk(self, nr):
        """
        Get the primary key for a certain requirement name
        :param nr: the requirement name
        :return: the primary key
        """
        for item in self.global_fixture.get('requirementname'):
            if item.get('fields').get('requirement_number') == nr:
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
            part = dict(fields=dict(version_number=version),
                        model='level.asvsversion',
                        pk=pk + 1)
            fixture.append(part)
        self.global_fixture.update({'version': fixture})
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
            if not category.get('deprecationNotice'):
                part = dict(fields=dict(category_number=int(nr),
                                        lang_code=lang_code[0],
                                        name=cat_name, ),
                            model='level.categoryname',
                            pk=pk + 1)
                fixture.append(part)
        self.global_fixture.update({'categoryname': fixture})
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
            category = self.reader.get('chapters').get(nr)
            if not category.get('deprecationNotice'):
                part = dict(
                    fields=dict(name=self._get_category_name_pk(nr),
                                number=nr,
                                version=self._get_version_pk()),
                    model='level.category', pk=pk + 1)
                fixture.append(part)
        self.global_fixture.update({'category': fixture})
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
        pk = 1
        for key, value in sorted(self.reader.get('levelNames').items()):
            lang_code = list(value)[0][0:]
            name = value.get(lang_code)
            part = dict(fields=dict(lang_code=lang_code,
                                    level_number=key,
                                    name=name),
                        model='level.levelname',
                        pk=pk)
            fixture.append(part)
            pk += 1
        self.global_fixture.update({'levelname': fixture})
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
        self.global_fixture.update({'level': fixture})
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
                                    category=self._get_category_name_pk(
                                        item.get('chapterNr')),
                                    title=item.get('title').get(lang_code[0])),
                        model='level.requirementname',
                        pk=pk + 1)
            fixture.append(part)
        self.global_fixture.update({'requirementname': fixture})
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
            part = dict(
                fields=dict(requirement_name=self._get_requirement_name_pk(
                    item.get('nr')),
                    version=self._get_version_pk()),
                model='level.requirement',
                pk=pk + 1)
            fixture.append(part)
        self.global_fixture.update({'requirement': fixture})
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))
