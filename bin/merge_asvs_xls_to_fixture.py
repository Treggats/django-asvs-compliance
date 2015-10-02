#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from os.path import dirname, realpath


DIR = dirname(realpath(__file__))
categories_str = DIR + "/../levels/fixtures/categories.json"


def search_category_pk(version):

    """
    search for the pk of a category
    """

    with open(categories_str, "r") as categories_file:
        categories = json.load(categories_file)
    for item in categories:
        if item["fields"]["version"] == version:
            pk = item["pk"]
            return pk


def create_requirements():
    pk = 1
    output = []
    with open(DIR + "/asvs_v2_xls.json", "r") as asvs_xls_file:
        asvs_xls = json.load(asvs_xls_file)
        for item in asvs_xls:
            nr = item["ASVS Item #"].split(".")[0]
            levels = []
            if item["Level 1"] == "Y":
                levels.append(1)
            if item["Level 2"] == "Y":
                levels.append(2)
            if item["Level 3"] == "Y":
                levels.append(3)

            description = item["Requirement"]
            output.append({
                "fields": {
                    "category": search_category_pk(nr),
                    "description": description,
                    "number": levels
                },
                "model": "levels.requirement",
                "pk": pk
            })
            pk += 1
    return json.dumps(output,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))

with open(DIR + "/../requirements.json", "w") as out:
    out.write(create_requirements())
