# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-10 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hurumap', '0005_auto_20180610_1640'),
        ('takwimu', '0004_auto_20180610_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPageDataIndicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hurumap.DataIndicator')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_indicators', to='takwimu.TopicPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='topicpagedata',
            name='indicator',
        ),
        migrations.RemoveField(
            model_name='topicpagedata',
            name='page',
        ),
        migrations.DeleteModel(
            name='TopicPageData',
        ),
    ]
