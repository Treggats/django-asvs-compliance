from django.core.management.base import BaseCommand

import os
from pathlib import Path



from level.management.helpers.asvs import ASVS
from level.management.helpers.aasvs import AASVS

class Command(BaseCommand):
    """
    """

    def handle(self, *args, **options):
        print('Baaa')

        data_dir = 'django_asvs_compliance'
        try:
            project_path = Path(os.environ[data_dir])
            asvs_file = "{}/bin/helpers/asvs.json".format(project_path)
            aasvs_file = "{}/bin/helpers/aasvs.json".format(project_path)
            asvs = ASVS(asvs_file)
            aasvs = AASVS(aasvs_file)
            print(aasvs)
            # fc = FixtureCreator(asvs_file)
            # fixture = fc.annotated_fixture()
            # print(fixture)
            # import ipdb; ipdb.set_trace()
        except KeyError:
            print("Data dir '{}' has not been set.".format(data_dir))
