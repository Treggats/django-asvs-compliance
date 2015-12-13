# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from pathlib import Path
from asvsannotation.management.helpers.aasvs import AASVS


class Command(BaseCommand):
    help = 'Load AASVS data from a json file or a directory'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)
        parser.add_argument('--help-dir', type=str)

    def handle(self, *args, **options):
        if options['help_dir']:
            help_dir = Path(options['help_dir']).resolve()
            aasvs = AASVS()
            aasvs.process_data(str(help_dir))
        else:
            self.args = '--file aasvs.json', '--dir owasp-aasvs/src/help'
            self.stdout.write(self.usage('loadaasvsdata'))
