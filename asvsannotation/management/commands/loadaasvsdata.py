# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from pathlib import Path
from asvsannotation.management.helpers.aasvs import AASVS


class Command(BaseCommand):
    help = 'Load AASVS data from a json file or a directory'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)
        parser.add_argument('--dir', type=str)

    def handle(self, *args, **options):
        if options['file']:
            json_file = Path(options['file']).resolve()

            aasvs = AASVS(str(json_file))
            aasvs.load_requirement()
        elif options['dir']:
            dir = Path(options['dir']).resolve()
            aasvs = AASVS()
            aasvs.load_help_text(str(dir))
        else:
            self.args = '--file aasvs.json', '--dir owasp-aasvs/src/help'
            self.stdout.write(self.usage('loadaasvsdata'))
