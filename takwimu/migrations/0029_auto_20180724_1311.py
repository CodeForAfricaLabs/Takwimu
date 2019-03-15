# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-24 10:11
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0028_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explainersteps',
            name='steps',
            field=wagtail.wagtailcore.fields.StreamField([(b'step', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'brief', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Background colour.', required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'sidebar', wagtail.wagtailcore.blocks.RichTextBlock(required=False))], icon=b'user'))]),
        ),
    ]
