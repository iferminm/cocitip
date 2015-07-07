import datetime

from haystack import indexes

from tweets.models import Tweet


class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    """docstring for TweetIndex"""
    account = indexes.CharField(model_attr='account')
    posted_on = indexes.DateTimeField(model_attr='posted_on')
    text = indexes.CharField(document=True, model_attr='text')

    def get_model(self):
        """docstring for get_model"""
        return Tweet

    def index_queryset(self, using=None):
        """docstring for index_queryset"""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())

