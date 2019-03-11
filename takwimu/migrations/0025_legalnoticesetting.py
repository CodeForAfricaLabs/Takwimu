# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-23 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('takwimu', '0024_auto_20180717_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalNoticeSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_use', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('privacy_policy', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('cookie_policy', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Legal Notice',
            },
        ),
    ]
