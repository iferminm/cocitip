import datetime
import time
import csv

from django.core.management.base import BaseCommand, CommandError

from tweets.models import Tweet


class Command(BaseCommand):
    """Imports tweets from a file in a standard format,
    could json or csv. Only CSV supporten by the moment
    """
    supported_types = ('csv',)
    date_format = '%Y-%m-%d %H:%M:%S'

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='file_path', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file_path')
        file_type = file_path.split('.')[-1]

        if file_type not in self.supported_types:
            raise Exception('File type not supported')

        if file_type == 'csv':
            self.import_from_csv(file_path)


    def import_from_csv(self, path):
        file_name = path.split('/')[-1]
        account = file_name.split('_')[0]
        with open(path, 'r') as csvfile:
            header = csvfile.readline()
            reader = csv.reader(csvfile)
            for row in reader:
                tw_id, date_str, text = row
                time_struct = time.strptime(date_str, self.date_format)
                date = datetime.datetime.fromtimestamp(time.mktime(time_struct))

                tweet = Tweet(
                    account=account,
                    twitter_id=tw_id,
                    posted_on=date,
                    text=text
                )
                tweet.save()
                
                message = 'Saved tweet {0} from account {1}'.format(tw_id, account)
                print(message)

