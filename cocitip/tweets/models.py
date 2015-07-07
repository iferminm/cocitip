from django.db import models


class CreatedUpdatedAtAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tweet(CreatedUpdatedAtAbstractModel):
    """docstring for Tweet"""
    account = models.CharField(max_length=36)
    twitter_id = models.BigIntegerField(unique=True)
    posted_on = models.DateTimeField()
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return '{0}-{1}'.format(self.account, self.twitter_id)

    def __str__(self):
        return str(self.__unicode__())
