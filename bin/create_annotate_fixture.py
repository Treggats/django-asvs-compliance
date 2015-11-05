#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from codecs import open
import json
from helpers.asvs import ASVS


class FixtureCreator(object):

    """
    FixtureCreator

    Open a csv file
    """

    def __init__(self, json_file, version=1):
        self.DEBUG = False
        self.json_file = open(json_file, encoding='utf-8')
        self.version = version
        self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def version_fixture(self):
        '''
        Example fixture
        [
            {
                "fields": {
                    "version": "3"
                },
                "model": "level.version",
                "pk": 1
            }
        ]
        '''
        fixture = list()
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def annotated_title_fixture(self):
        """
        Example fixture
        [
            {
                "fields": {
                    "lang_code": "en",
                    "title": "Strongly encrypted transport"
                },
                "model": "level.annotationtitle",
                "pk": 1
            }
        ]
        """
        fixture = list()
        for pk, item in enumerate(self.reader['requirements']):
            key = list(item.get('shortTitle').keys())[0]
            title = item.get('shortTitle').get(key)
            fixture.append(dict(fields=dict(
                           lang_code=key,
                           title=title),
            model='level.annotationtitle',
            pk=pk + 1))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def annotated_related_fixture(self):
        '''
        Example fixture
        [
            {
                "fields": {
                    "name": "Security Stackexchange: Forgotten password or reset link, which is more secure to email",
                    "url": "http://security.stackexchange.com/questions/13026/forgotten-password-or-reset-link-which-is-more-sec"
                },
                "model": "level.annotationrelated",
                "pk": 1
            }
        ]
        '''
        fixture = list()
        for pk, item in enumerate(self.reader.get('requirements')):
            related = item.get('related')
            if related:
                if related[0].get('name') and related[0].get('url'):
                    fixture.append(dict(fields=dict(
                                   name=related[0].get('name'),
                                   url=related[0].get('url')),
                    model='level.annotationrelated',
                    pk=pk + 1))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

    def annotated_fixture(self):
        """
        Example fixture
        [
            {
                "fields": {
                    "category": 2,
                    "related": null,
                    "requirement": [
                        4,
                        8,
                        10
                    ],
                    "title": "short title"
                },
                "model": "level.annotation",
                "pk": 1
            }
        ]
        """
        fixture = list()
        for pk, item in enumerate(self.reader['requirements']):
            print("%i: %s" % (pk, item))
            """
            fixture.append(dict(fields=dict(
                category=None,
                related=None,
                requirement=None,
                title=None
            ),
            model='level.annotation',
            pk=pk + 1))

        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))
        """


if __name__ == "__main__":
    data_dir = 'django_asvs_compliance'
    try:
        project_path = Path(os.environ[data_dir])
        aasvs_file = "{}/bin/helpers/asvs.json".format(project_path)
        aasvs = ASVS(aasvs_file)
        print(aasvs)
        # fc = FixtureCreator(asvs_file)
        # fixture = fc.annotated_fixture()
        # print(fixture)
        # import ipdb; ipdb.set_trace()
    except KeyError:
        print("Data dir '{}' has not been set.".format(data_dir))
