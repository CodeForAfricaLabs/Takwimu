"""
Signals to index topics on creation of ProfileSectionPage and ProfilePage

Should save
    - page type/class : either ProfileSectionPage or ProfilePage
    - topic_id
    - topic_body
    - parent_page_id
    - category
    - country
"""

from takwimu.models import ProfilePage, ProfileSectionPage
from django.dispatch import receiver
from wagtail.wagtailcore.signals import page_published

from takwimu.search.takwimu_search import TakwimuTopicSearch
from takwimu.search.utils import get_widget_data, get_page_details


@receiver(page_published, sender=ProfilePage)
@receiver(page_published, sender=ProfileSectionPage)
def index_new_changes_in_profilepage(sender, instance, created, **kwargs):
    search_backend = TakwimuTopicSearch()
    country, category, parent_page_type = get_page_details(instance)

    parent_page_id = instance.id
    for topic in instance.body.stream_data:
        topic_id = topic.get('id')
        topic_body = topic['value'].get('body', '')
        topic_summary = topic['value'].get('summary', '')
        body = topic_body + " " + topic_summary

        result, outcome = search_backend.add_to_index(category,
                                                      body,
                                                      country,
                                                      parent_page_id,
                                                      parent_page_type,
                                                      type="topic",
                                                      topic_id=topic_id)

        indicators = topic['value'].get('indicators', '')
        for indicator in indicators:
            for widget in indicator['value']['widgets']:
                data = get_widget_data(widget)
                if data:
                    result, outcome = search_backend.add_to_index(
                        category,
                        data.get('body'),
                        country,
                        parent_page_id,
                        parent_page_type,
                        type='indicator_widget',
                        widget_id=data.get(
                            'widget_id'))