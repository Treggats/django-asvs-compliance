# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from pathlib import Path
from asvsannotation.management.helpers.aasvs import AASVS


class Command(BaseCommand):
    help = 'Load AASVS data from a json file or a directory'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)
        parser.add_argument('--src-dir', type=str)

    def handle(self, *args, **options):
        if options['src_dir']:
            src_dir = Path(options['src_dir']).resolve()
            aasvs = AASVS(str(src_dir))
            aasvs.process_annotations()
        else:
            self.args = '--src-dir owasp-aasvs/src'
            self.stdout.write(self.usage('loadaasvsdata'))
