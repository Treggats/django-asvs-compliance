#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from codecs import open
from unicodedata import name as uni_name
import csv
import json


class FixtureCreator(object):

    """
    FixtureCreator

    Open a csv file
    """

    def __init__(self, csv_file):
        self.DEBUG = False
        self.categories = {}
        self.requirements = []
        self.rows = []
        self.levels = []
        self.csv_file = open(csv_file, encoding='utf-8')

        self.reader = csv.DictReader(self.csv_file, skipinitialspace=True)
        self.csv_to_rows()
        self.create_categories()
        self.create_requirements()
        self.create_levels()

    def __del__(self):
        """Close the csv file"""
        self.csv_file.close()

    def _replace_char(self, variable, char=None, new_char=None):
        """Replace unicode character with something else"""
        if char is None:
            char = u'\u2713'
        if new_char is None:
            new_char = "Y"
        if uni_name(variable) == uni_name(char):
            return new_char
        return variable

    def csv_to_rows(self):
        """Put the contents of the csv in rows"""
        for row in self.reader:
            """Replace unicode character"""
            if row.get("Level 1"):
                row["Level 1"] = self._replace_char(row.get("Level 1"))
            if row.get("Level 2"):
                row["Level 2"] = self._replace_char(row.get("Level 2"))
            if row.get("Level 3"):
                row["Level 3"] = self._replace_char(row.get("Level 3"))
            self.rows.append(row)

    def create_levels(self):
        self.levels.append(dict(en="Oppertunistic"))
        self.levels.append(dict(en="Standard"))
        self.levels.append(dict(en="Advanced"))

    def create_categories(self):
        for row in self.rows:
            item = dict(en=row["Detailed Verification Requirement"])
            if row["ID"].startswith("V") and "section" not in item:
                index = int(row["ID"][1:])
                self.categories[index] = item

    def create_requirements(self):
        for row in self.rows:
            if not row["ID"].startswith("V"):
                chapterNr = row["ID"].split(".")[0]
                nr = row["ID"].split(".")[1]
                levels = []
                if row.get("Level 1") == "Y":
                    levels.append(1)
                if row.get("Level 2") == "Y":
                    levels.append(2)
                if row.get("Level 3") == "Y":
                    levels.append(3)
                title_dict = dict(en=row["Detailed Verification Requirement"])
                self.requirements.append(dict(
                                         chapterNr=chapterNr,
                                         nr=nr,
                                         levels=levels,
                                         title=title_dict))

    def generate_level_fixture(self):
        fixture = []
        for key, lvl in enumerate(self.levels):
            fixture.append(dict(
                           fields=dict(number=key + 1,
                                       name=lvl["en"]),
                           model="levels.levelnumber",
                           pk=key + 1))
        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

    def generate_category_fixture(self):
        fixture = []
        for key in self.categories:
            item = self.categories[key]
            fixture.append(dict(fields=dict(version="V{}".format(key),
                           name=item["en"]),
                model="levels.category",
                pk=key))

        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

    def generate_requirement_fixture(self):
        fixture = []
        for pk, req in enumerate(self.requirements):
            fixture.append(dict(fields=dict(
                           category=int(req["chapterNr"]),
                           description=req["title"]["en"],
                           number=req["levels"]),
                model="levels.requirement",
                pk=pk + 1))

        return json.dumps(fixture,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

if __name__ == "__main__":
    data_dir = 'django_asvs_compliance'
    try:
        project_path = Path(os.environ[data_dir])
        lvl_fixt_path = "{}/levels/fixtures".format(project_path)
        asvs_file = "{}/bin/asvs_v3_xls.csv".format(project_path)
        lvl_fixt_file = "{}/levels.json".format(lvl_fixt_path)
        cat_fixt_file = "{}/categories.json".format(lvl_fixt_path)
        req_fixt_file = "{}/requirements.json".format(lvl_fixt_path)
        fc = FixtureCreator(asvs_file)
        """Use a write operation to create files"""
        with open(lvl_fixt_file, "w") as outfile:
            lvl_fixt = fc.generate_level_fixture()
            outfile.write(lvl_fixt)
        with open(cat_fixt_file, "w") as outfile:
            cat_fixt = fc.generate_category_fixture()
            outfile.write(cat_fixt)
        with open(req_fixt_file, "w") as outfile:
            req_fixt = fc.generate_requirement_fixture()
            outfile.write(req_fixt)
    except KeyError:
        print("Data dir '{}' has not been set.".format(data_dir))
