# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from level.management.helpers.aasvs import AASVS


class Command(BaseCommand):
    help = 'Load AASVS data from a json file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        if not options['file']:
            self.args = '--file aasvs.json'
            self.stdout.write(self.usage('loadaasvsdata'))
        else:
            json_file = Path(options['file']).resolve()

            aasvs = AASVS(str(json_file))
            aasvs.load_requirement()
