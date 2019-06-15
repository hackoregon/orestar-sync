from django.core.management.base import BaseCommand
from ...models import Transactions
import csv

class Command(BaseCommand):
    help = 'Load collected CSV files into database'

    def handle(self, *args, **kwargs):
        with open('20190614-191757.csv', 'r') as csvfile:
            for row in csvfile:
                column = row.strip('\n').split(',')

                t = Transactions(
                    transaction_id = int(column[0]),
                    transaction_date = '{}-{}-{}'.format(column[1][6:], column[1][:2], column[1][3:5]),
                    status = column[2], 
                    filer_committee = column[3], 
                    contributor_payee = column[4], 
                    transaction_subtype = column[5], 
                    amount = float(column[6].replace('$', '').replace('"', ''))
                )

                t.save()
                self.stdout.write('{} loaded'.format(column[0]))