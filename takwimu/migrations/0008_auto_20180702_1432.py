# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-02 11:32
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0007_auto_20180702_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilesectionpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'topic', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'icon', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'summary', wagtail.core.blocks.TextBlock(required=False)), (b'body', wagtail.core.blocks.RichTextBlock(required=False))]))], blank=True),
        ),
        migrations.AddField(
            model_name='profilesectionpage',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name=b'Last Updated'),
        ),
    ]
