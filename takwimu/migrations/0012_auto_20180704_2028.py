# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-04 17:28
from __future__ import unicode_literals

from django.db import migrations
import takwimu.models.dashboard
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0011_auto_20180704_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'topic', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'icon', takwimu.models.dashboard.IconChoiceBlock(required=False)), (b'summary', wagtail.core.blocks.TextBlock(required=False)), (b'body', wagtail.core.blocks.RichTextBlock(required=False)), (b'indicators', wagtail.core.blocks.StreamBlock([(b'free_form', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'body', wagtail.core.blocks.RichTextBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'snippet', template=b'takwimu/_includes/dataview/freeform.html')), (b'data_indicator', takwimu.models.dashboard.DataIndicatorChooserBlock()), (b'embed', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'embed', wagtail.embeds.blocks.EmbedBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'media', template=b'takwimu/_includes/dataview/embed.html')), (b'document', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'doc-full', template=b'takwimu/_includes/dataview/document.html')), (b'image', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'caption', wagtail.core.blocks.TextBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'image', template=b'takwimu/_includes/dataview/image.html')), (b'html', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'raw_html', wagtail.core.blocks.RawHTMLBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'code', template=b'takwimu/_includes/dataview/code.html')), (b'entities', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'entities', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([(b'name', wagtail.core.blocks.CharBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'description', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))]))), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'group', template=b'takwimu/_includes/dataview/entities.html'))], required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='profilesectionpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'topic', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'icon', takwimu.models.dashboard.IconChoiceBlock(required=False)), (b'summary', wagtail.core.blocks.TextBlock(required=False)), (b'body', wagtail.core.blocks.RichTextBlock(required=False)), (b'indicators', wagtail.core.blocks.StreamBlock([(b'free_form', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'body', wagtail.core.blocks.RichTextBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'snippet', template=b'takwimu/_includes/dataview/freeform.html')), (b'data_indicator', takwimu.models.dashboard.DataIndicatorChooserBlock()), (b'embed', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'embed', wagtail.embeds.blocks.EmbedBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'media', template=b'takwimu/_includes/dataview/embed.html')), (b'document', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'doc-full', template=b'takwimu/_includes/dataview/document.html')), (b'image', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'caption', wagtail.core.blocks.TextBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'image', template=b'takwimu/_includes/dataview/image.html')), (b'html', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'raw_html', wagtail.core.blocks.RawHTMLBlock(required=False)), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'code', template=b'takwimu/_includes/dataview/code.html')), (b'entities', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'entities', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([(b'name', wagtail.core.blocks.CharBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'description', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))]))), (b'source', wagtail.core.blocks.RichTextBlock(features=[b'link'], required=False))], icon=b'group', template=b'takwimu/_includes/dataview/entities.html'))], required=False))]))], blank=True),
        ),
    ]
