# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-17 14:36
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicpage',
            name='parent_topic',
        ),
        migrations.RemoveField(
            model_name='topicpage',
            name='related_topics',
        ),
    ]
