# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-12 11:39
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0021_socialmediasetting_supportsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportsetting',
            name='address',
            field=wagtail.core.fields.RichTextField(blank=True, help_text=b'TAKWIMU address', null=True),
        ),
    ]
