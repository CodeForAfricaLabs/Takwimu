# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-09 13:04
from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0017_faq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='faq',
            name='cta_one_url',
            field=models.URLField(default=b'https://takwimu.zendesk.com/', verbose_name=b"'Find Out More' button URL"),
        ),
        migrations.AddField(
            model_name='faq',
            name='cta_two_name',
            field=models.TextField(blank=True, verbose_name=b'Second button Name (optional)'),
        ),
        migrations.AddField(
            model_name='faq',
            name='cta_two_url',
            field=models.URLField(blank=True, verbose_name=b'Second button URL (optional)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
