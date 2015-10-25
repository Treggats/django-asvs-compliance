#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from codecs import open
import csv
import json


class FixtureCreator(object):

    """
    FixtureCreator

    Open a csv file
    """

    def __init__(self, csv_file):
        self.DEBUG = False
        self.csv_file = open(csv_file, encoding='utf-8')
        self.csv = csv.reader(self.csv_file,
                              delimiter=',',
                              quotechar='"')
        self.categories = []
        self.requirements = []
        self.rows = []
        """Skip the first line of the csv
        those are field markers.
        TODO: there must be a better way to do this.
        """
        self.reader = iter(self.csv)
        next(self.reader)

        self.csv_to_rows()
        self.create_categories()
        self.create_requirements()

    def __del__(self):
        """Close the csv file"""
        self.csv_file.close()

    def _replace_char(self, variable, char=None, new_char=None):
        """Replace unicode character with something else"""
        if char is None:
            char = 10003
        if new_char is None:
            new_char = "Y"
        if ord(variable) == char:
            return new_char
        return variable

    def csv_to_rows(self):
        """Put the contents of the csv in rows"""
        for row in self.reader:
            """Replace unicode character"""
            if row[2]:
                row[2] = self._replace_char(row[2])
            if row[3]:
                row[3] = self._replace_char(row[3])
            if row[4]:
                row[4] = self._replace_char(row[4])
            self.rows.append(row)

    def create_categories(self):
        for row in self.rows:
            if row[0].startswith("V") and "section" not in row[1]:
                self.categories.append(dict(
                                       version=row[0],
                                       description=row[1]))
        if self.DEBUG:
            return json.dumps(self.categories, sort_keys=True, indent=4)

    def _get_category_pk(self, version):
        for k, x in enumerate(self.categories):
            if x.get("version") == "V1":
                return k+1

    def create_requirements(self):
        for row in self.rows:
            if not row[0].startswith("V"):
                self.requirements.append(dict(
                                         id=row[0],
                                         description=row[1],
                                         level_1=row[2],
                                         level_2=row[3],
                                         level_3=row[4]))
        if self.DEBUG:
            return json.dumps(self.requirements, sort_keys=True, indent=4)

    def generate_level_fixture(self):
        levels = []
        levels.append(
                      dict(
                           fields=dict(
                                       number=1,
                                       name="Oppertunistic"),
                           model="levels.levelnumber",
                           pk=1))
        levels.append(
                      dict(
                           fields=dict(
                                       number=1,
                                       name="Standard"),
                           model="levels.levelnumber",
                           pk=2))
        levels.append(
                      dict(
                           fields=dict(
                                       number=1,
                                       name="Advanced"),
                           model="levels.levelnumber",
                           pk=3))
        return json.dumps(levels,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

    def generate_category_fixture(self):
        output = []
        for pk, item in enumerate(self.categories):
            output.append(
                          dict(
                               fields=dict(
                                           version=item.get("version"),
                                           name=item.get("description")),
                               model="levels.category",
                               pk=pk+1))
        return json.dumps(output,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

    def generate_requirement_fixture(self):
        output = []
        for pk, item in enumerate(self.requirements):
            levels = []
            id = "V{}".format(item["id"].split('.')[0])
            if item["level_1"] == "Y":
                levels.append(1)
            if item["level_2"] == "Y":
                levels.append(2)
            if item["level_3"] == "Y":
                levels.append(3)
            output.append(
                          dict(
                               fields=dict(
                                           category=self._get_category_pk(id),
                                           description=item["description"],
                                           number=levels),
                               model="levels.requirement",
                               pk=pk + 1))
        return json.dumps(output,
                          sort_keys=True,
                          indent=4,
                          separators=(',', ': '))

if __name__ == "__main__":
    data_dir = 'django_asvs_compliance'
    try:
        project_path = Path(os.environ[data_dir])
        asvs_file = "{}/bin/asvs_v3_xls.csv".format(project_path)
        lvl_fixt_file = "{}/levels/fixtures/levels.json".format(project_path)
        cat_fixt_file = "{}/levels/fixtures/categories.json".format(project_path)
        req_fixt_file = "{}/levels/fixtures/requirements.json".format(project_path)
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
