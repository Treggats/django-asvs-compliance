# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from level.management.helpers.asvs import ASVS


class Command(BaseCommand):
    help = 'Load ASVS data from a json file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)
        parser.add_argument('--type', type=str)
        parser.add_argument('--asvs_version', type=str)

    def handle(self, **options):
        if options['file'] is None or options['type'] is None:
            self.stdout.write('Arguments for this command are:\n'
                              ' --file (a json file)\n'
                              ' --type (version, level, category, '
                              'requirement)\n'
                              ' --asvs_version (optional, defaults to 3)\n'
                              'The order of --type is important')
        else:
            self.json = options['file']
            if not options['asvs_version']:
                asvs = ASVS(self.json, 3)
            else:
                asvs = ASVS(self.json, options['asvs_version'])

            if options['type'] == 'version':
                asvs.load_version()
            elif options['type'] == 'level':
                asvs.load_level()
            elif options['type'] == 'category':
                asvs.load_category()
            elif options['type'] == 'requirement':
                asvs.load_requirement()
            else:
                raise CommandError('Could not understand type: {}'.format(options['type']))
