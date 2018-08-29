# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-16 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('takwimu', '0034_profilepage_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faqs', wagtail.wagtailcore.fields.StreamField([(b'faq', wagtail.wagtailcore.blocks.StructBlock([(b'question', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'answer', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'cta_one_url', wagtail.wagtailcore.blocks.URLBlock(default=b'https://takwimu.zendesk.com/', help_text=b"'Find Out More' button URL")), (b'cta_two_name', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Second button Name (optional)', required=False)), (b'cta_two_url', wagtail.wagtailcore.blocks.URLBlock(help_text=b'Second button URL (optional)', required=False))]))], blank=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'FAQ',
            },
        ),
    ]