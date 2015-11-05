#!/usr/bin/env python
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
        for pk, value in enumerate(self.reader):
            str += json.dumps(value, indent=4) + "\n"
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
        :return: a Django fixture representation
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
