#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json


class FixtureCreator(object):
    """
    FixtureCreator

    Create a new instance with a csv input file
    """
    def __init__(self, csv_file):
        self.csv_file = csv.reader(csv_file,
                                   delimiter=',',
                                   quotechar='"')
        self.categories = []
        self.requirements = []
        self.rows = []
        """Skip the first line of the csv
        those are field markers
        """
        self.reader = iter(self.csv_file)
        next(self.reader)

        self.csv_to_rows()

    """Put the contents of the csv in rows"""
    def csv_to_rows(self):
        for row in self.reader:
            self.rows.append(row)

    def create_categories(self):
        for row in self.rows:
            if row[0].startswith("V") and "section" not in row[1]:
                self.categories.append({row[0]: row[1]})

    def create_requirements(self):
        for row in self.rows:
            if not row[0].startswith("V"):
                self.requirements.append(dict(
                                         id=row[0],
                                         description=row[1],
                                         level_1=row[2],
                                         level_2=row[3],
                                         level_3=row[4]))
        return json.dumps(self.requirements, sort_keys=True, indent=4)

with open("asvs_v3_xls.csv") as asvs_file:
    fc = FixtureCreator(asvs_file)
    cats = fc.create_categories()
    # print(cats)
    reqs = fc.create_requirements()
    print(reqs)
    asvs_file.close()


"""
def replace_character(var):
    return var.decode("utf-8").replace(u"\u2713", "Y").encode("utf-8")


def create_fixture(filename, data):
    with open(filename, "w") as out_file:
        json.dump(data, out_file,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))

with open("asvs_v3_xls.csv", "rb") as csv_file:
    spamreader = csv.reader(csv_file, delimiter=",", quotechar='"')
    sr = iter(spamreader)
    next(sr)
    categories = {}
    requirements = []
    for row in sr:
        if row[0].startswith("V"):
            if "section" not in row[1]:
                categories[row[0]] = row[1]
        else:
            cat_id = row[0].split('.')[0]
            row_id = row[0].split('.')[1]
            category = categories.get("V{}".format(cat_id))
            if DEBUG and int(cat_id) < 10:
                cat_id = "0{}".format(cat_id)
            if DEBUG and int(row_id) < 10:
                row_id = "0{}".format(row_id)
            requirements_format = "V{}.{}".format(cat_id, row_id)
            requirements.append(dict(category_id=cat_id,
                                category=category,
                                requirement=row[1],
                                req_id=requirements_format,
                                level_1=replace_character(row[2]),
                                level_2=replace_character(row[3]),
                                level_3=replace_character(row[4])))

    output = []
    for pk, value in enumerate(categories.items()):
        output.append({
                      "fields": {
                          "version": value[0],
                          "name": value[1]
                      },
                      "model": "levels.category",
                      "pk": pk + 1
                      })
    print(json.dumps(output, sort_keys=True, indent=4))

    data = requirements
    output = []
    for pk, item in enumerate(data):
        levels = []
        if item["level_1"] == "Y":
            levels.append(1)
        if item["level_2"] == "Y":
            levels.append(2)
        if item["level_3"] == "Y":
            levels.append(3)
        output.append({
                      "fields": {
                          "category": item["category_id"],
                          "description": item["requirement"],
                          "number": levels
                      },
                      "model": "levels.requirement",
                      "pk": pk + 1
                      })
    create_fixture("requirements.json", output)
"""
