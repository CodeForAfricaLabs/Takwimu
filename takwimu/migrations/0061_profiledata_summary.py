# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 04:13
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0060_profiledata'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='summary',
            field=wagtail.core.fields.RichTextField(default=''),
        ),
    ]
