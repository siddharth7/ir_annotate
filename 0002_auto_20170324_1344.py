# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetinfo',
            name='tweet_agression',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='tweetinfo',
            name='tweet_id',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tweetinfo',
            name='tweet_text',
            field=models.CharField(max_length=1000),
        ),
#         migrations.AlterField(
#             model_name='tweetinfo',
#             name='tweet_text',
#             field=models.CharField(max_length=1000),
#         ),
    ]
