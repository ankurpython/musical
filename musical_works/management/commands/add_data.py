import math

from django.core.management import BaseCommand
import pandas as pd

from musical_works.models import MusicalMetadata
from musical_works.serializers import MusicalSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_csv('musical_works/works_metadata.csv')
        for k in range(len(df)):
            dt = dict(df.loc[k].fillna(0))

            dt['contributors'] = dt['contributors'].split('|')
            if dt['iswc']:
                if MusicalMetadata.objects.filter(iswc=dt['iswc']).exists():
                    obj = MusicalMetadata.objects.get(iswc=dt['iswc'])
                    for ctb in dt['contributors']:
                        if ctb not in obj.contributors:
                            obj.contributors.append(ctb)
                            obj.save()
                else:
                    serializer = MusicalSerializer(data=dt)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)

        return "done"
