# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0021_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='calendarpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='CalendarPage',
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
    ]
