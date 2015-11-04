#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from codecs import open
import json


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

    def annotated_fixture(self):
        fixture = []
        for item in self.reader['requirements']:
            print(item)
        '''
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
        '''


if __name__ == "__main__":
    data_dir = 'django_asvs_compliance'
    try:
        project_path = Path(os.environ[data_dir])
        asvs_file = "{}/bin/aasvs.json".format(project_path)
        fc = FixtureCreator(asvs_file)
        fc.annotated_fixture()
        # import ipdb; ipdb.set_trace()
    except KeyError:
        print("Data dir '{}' has not been set.".format(data_dir))
