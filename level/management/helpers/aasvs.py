#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from codecs import open


class AASVS(object):
    def __init__(self, file):
        self.json_file = open(file, encoding='utf-8')
        self.reader = json.load(self.json_file)

    def __del__(self):
        """Close the csv file"""
        self.json_file.close()

    def __str__(self):
        str = ""
        for pk, value in enumerate(self.reader.get('requirements')):
            str += json.dumps(value, indent=4) + "\n"
        return str