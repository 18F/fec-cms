# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_merge_20170127_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordpage',
            name='advisory_opinion',
            field=models.CharField(blank=True, default='', help_text="If this is an article about an AO, specify the AO number, e.g. '2016-20'", max_length=255),
        ),
    ]
