# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-22 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0064_contactpage_snippets'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataByTopicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('country', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wazimap.Geography')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
