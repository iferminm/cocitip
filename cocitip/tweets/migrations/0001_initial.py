# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.CharField(max_length=36)),
                ('twitter_id', models.PositiveIntegerField()),
                ('posted_on', models.DateTimeField()),
                ('text', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
