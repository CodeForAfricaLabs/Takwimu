import json
import uuid

from django.core.serializers.json import DjangoJSONEncoder
from wagtail.core.blocks import StreamValue
from django.db import migrations


def indicator_to_indicator_widget(topic):
    """
    Migrate Indicators in non-versioned Topic to Indicator widgets (Topic v2).
    """

    indicators = []
    version = topic['value'].get('version')
    if not version:
        current_indicators = topic['value'].get('indicators')
        for current_indicator in current_indicators:
            # Current indicator becomes the first widget in indicator v2
            indicators.append({
                'type': 'indicators',
                'id': str(uuid.uuid1()),
                'value': {
                    'title': current_indicator['value']['title'],
                    'widgets': [current_indicator],
                }
            })
        if current_indicators:
            topic['value']['indicators'] = indicators
        topic['value']['version'] = 'v2'
    return topic


def indicator_widget_to_indicator(topic):
    """
    Migrate Indicators widgets in Topic v2 back to Indicator (and non-versioned Topic).
    """

    indicators = []
    version = topic['value'].get('version')
    if version and version.lower() == 'v2':
        current_indicators = topic['value'].get('indicators')
        for current_indicator in current_indicators:
            # Current widget was an indicator in indicator v1
            widgets = current_indicator['value'].get('widgets')
            if widgets:
                indicators.extend(widgets)
        del topic['value']['version']
        if current_indicators:
            topic['value']['indicators'] = indicators
    return topic


def get_stream_data(page, mapper):
    stream_data = []
    for topic in page.body.stream_data:
        stream_data.append(mapper(topic))

    return stream_data


def migrate(apps, mapper):
    ProfileSectionPage = apps.get_model('takwimu', 'ProfileSectionPage')
    for page in ProfileSectionPage.objects.all():
        stream_data = get_stream_data(page, mapper)
        raw_text = json.dumps(stream_data, cls=DjangoJSONEncoder)
        stream_block = page.body.stream_block
        page.body = StreamValue(stream_block, [], is_lazy=True,
                                raw_text=raw_text)
        page.save()

    ProfilePage = apps.get_model('takwimu', 'ProfilePage')
    for page in ProfilePage.objects.all():
        stream_data = get_stream_data(page, mapper)
        raw_text = json.dumps(stream_data, cls=DjangoJSONEncoder)
        stream_block = page.body.stream_block
        page.body = StreamValue(stream_block, [], is_lazy=True,
                                raw_text=raw_text)
        page.save()


def forwards(apps, schema_editor):
    migrate(apps, indicator_to_indicator_widget)


def backwards(apps, schema_editor):
    migrate(apps, indicator_widget_to_indicator)


class Migration(migrations.Migration):
    dependencies = [
        ('takwimu', '0037_faqsetting_data'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
