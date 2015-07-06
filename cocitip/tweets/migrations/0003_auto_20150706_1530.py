# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20150701_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='twitter_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
