# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from level.management.helpers.asvs import ASVS


class Command(BaseCommand):
    help = 'Load ASVS data from a json file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)
        parser.add_argument('--type', type=str)
        parser.add_argument('--asvs_version', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Arguments:\n'
                          ' --file (a json file)\n'
                          ' --type (level, category, requirement)\n'
                          ' --asvs_version (optional, defaults to 3)')
        if not options['file']:
            raise CommandError('No file was supplied.\n'
                               'Use the --file argument.')
        else:
            self.json = options['file']
            if not options['asvs_version']:
                asvs = ASVS(self.json, 3)
            else:
                asvs = ASVS(self.json, options['asvs_version'])

        if not options['type']:
            raise CommandError('No type was supplied.\n'
                               'Use the --type argument.\n'
                               'Possible values are:\n'
                               ' - level\n'
                               ' - category\n'
                               ' - requirement')
        else:
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
