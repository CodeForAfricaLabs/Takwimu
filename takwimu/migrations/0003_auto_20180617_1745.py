# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-17 14:45
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0002_auto_20180617_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportpagetopics',
            old_name='page',
            new_name='report_page',
        ),
        migrations.RenameField(
            model_name='reportsectionpagetopics',
            old_name='page',
            new_name='section_page',
        ),
    ]
