# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 09:58
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0052_aboutpage_methodology'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportservicessetting',
            name='overview',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
