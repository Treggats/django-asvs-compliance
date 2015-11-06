# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import os

from level.management.helpers.asvs import ASVS
from level.management.helpers.aasvs import AASVS


class Command(BaseCommand):
    """
    """

    def __init__(self):
        super().__init__()
        self.cls = None
        self.type_values = ('asvs', 'aasvs')

    help = "Create fixtures to load ASVS data into the models"

    def add_arguments(self, parser):
        parser.add_argument('--type', nargs='+', type=str)

    def handle(self, **options):
        json_path = os.path.realpath(__file__)
        commands_path = os.path.abspath(os.path.join(json_path, os.pardir))
        management_path = os.path.abspath(os.path.join(commands_path, os.pardir))
        if not options['type']:
            self.stdout.write("Argument --type ["+', '.join(
                self.type_values)+"] is not provided.")
        else:
            for type in options['type']:
                try:
                    if type == 'asvs':
                        asvs_file = "{}/helpers/asvs.json".format(management_path)
                        self.cls = ASVS(asvs_file)
                    elif type == 'aasvs':
                        aasvs_file = "{}/helpers/aasvs.json".format(management_path)
                        self.cls = AASVS(aasvs_file)
                    else:
                        self.cls = "The type values are: " + ", ".join(
                            self.type_values)
                    print(self.cls)
                except:
                    raise CommandError("Type: {} is not valid".format(type))
