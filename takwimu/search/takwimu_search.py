from collections import OrderedDict
import json

from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch_dsl import Search
from django.conf import settings

from takwimu.models import ProfilePage, ProfileSectionPage

DOC_TYPE = 'topic'


class TakwimuTopicSearch():

    def __init__(self):
        DEFAULT_SEARCH_BACKEND = settings.WAGTAILSEARCH_BACKENDS['default']

        self.es_index = DEFAULT_SEARCH_BACKEND['INDEX']
        self.es_timeout = DEFAULT_SEARCH_BACKEND['TIMEOUT']
        self.es_host_type = settings.TAKWIMU_ES_HOST_TYPE.lower()
        self.profilepages = ProfilePage.objects.live()
        self.profilesectionpages = ProfileSectionPage.objects.live()
        if self.es_host_type == 'aws':
            self.es_hosts = DEFAULT_SEARCH_BACKEND['HOSTS']
        else:
            self.es_hosts = DEFAULT_SEARCH_BACKEND['URLS']

        self.es = Elasticsearch(hosts=self.es_hosts)

    def reset_index(self):
        """Deletes old index (if any) and creates a new on"""

        try:
            self.es.indices.delete(self.es_index)
        except NotFoundError:
            pass
        self.es.indices.create(self.es_index,
                               settings.TAKWIMU_ES_INDEX_SETTINGS)

    def search(self, query_string, operator='or', country_filters=None,
               category_filters=None):
        """Search for query_string using operation applying country and/or category filters"""

        search = Search(using=self.es, index=self.es_index,
                        doc_type=DOC_TYPE).params(size=100)

        if operator == 'and':
            search = search.query('match_phrase', body=query_string)
        else:
            search = search.query('match', body=query_string)

        print('\n\n\n\n\n')
        print(country_filters)
        print(category_filters)
        print('\n\n\n\n\n')

        # Countries and categories may contain whitespace so don't join or
        # split on ' '.
        # Best approch is still to `try and see` rather than `checking`
        # https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
        try:
            countries = [i.lower() for i in country_filters]
            if countries:
                search = search.filter('terms', country=countries)
        except TypeError:
            pass
        try:
            categories = [i.lower() for i in category_filters]
            if categories:
                search = search.filter('terms', category=categories)
        except TypeError:
            pass

        results = []
        for hit in search.execute():
            hit = hit.to_dict()
            results.append({
                'category': hit['category'],
                'country': hit['country'],
                'region': 'National',
                'parent_page_id': hit['parent_page_id'],
                'parent_page_type': hit['parent_page_type'],
                'content_id': hit['content_id'],
                'content_type': hit['content_type'],
            })
        return results

    def add_to_index(self, category, body, country,
                     parent_page_id, parent_page_type, content_id, content_type):
        """
        - page type/class : either ProfileSectionPage or ProfilePage
        - category
        - body
        - country
        - parent_page_id
        - parent_page_type
        - content_id
        - content_type
        :return:
        """

        doc = {
            'category': category.title(),
            'body': body,
            'country': country.title(),
            'parent_page_id': parent_page_id,
            'parent_page_type': parent_page_type,
            'content_id': content_id,
            'content_type': content_type,
        }
        result = self.es.index(index=self.es_index, doc_type=DOC_TYPE, body=doc,
                               id=content_id)
        return result.get('result') == 'created', result
