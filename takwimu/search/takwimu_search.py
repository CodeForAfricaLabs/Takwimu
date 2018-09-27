from collections import OrderedDict
import json

from django.conf import settings
from django.utils.text import slugify

from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch_dsl import Search
from requests_aws4auth import AWS4Auth

from takwimu.models import ProfilePage, ProfileSectionPage

DOC_TYPE = 'topic'


def wordify(phrase):
    """
    Convert a given phrase into a single long word
    e.g. given `East African Community`, this method returns
    `eastafricancommunity` as one word.

    It is useful in search filters where spaces and `-` may be seen as word
    separators.
    """

    return slugify(phrase.strip()).replace('-', '')


class TakwimuTopicSearch():

    def __init__(self):
        DEFAULT_SEARCH_BACKEND = settings.WAGTAILSEARCH_BACKENDS['default']

        self.es_index = DEFAULT_SEARCH_BACKEND['INDEX']
        self.es_timeout = DEFAULT_SEARCH_BACKEND['TIMEOUT']
        HOST_TYPE = settings.TAKWIMU_ES_HOST_TYPE.lower()
        if HOST_TYPE == 'aws':
            DEFAULT_HOST = DEFAULT_SEARCH_BACKEND['HOSTS'][0]
            DEFAULT_OPTIONS = DEFAULT_SEARCH_BACKEND['OPTIONS']
            self.es = Elasticsearch(
                hosts=[{'host': DEFAULT_HOST['host'],
                        'port': DEFAULT_HOST['port']}],
                http_auth=DEFAULT_HOST['http_auth'],
                use_ssl=DEFAULT_HOST['use_ssl'],
                verify_certs=DEFAULT_HOST['verify_certs'],
                connection_class=DEFAULT_OPTIONS['connection_class']
            )
        else:
            DEFAULT_HOST = DEFAULT_SEARCH_BACKEND['URLS']
            self.es = Elasticsearch(hosts=DEFAULT_HOST)

        self.profilepages = ProfilePage.objects.live()
        self.profilesectionpages = ProfileSectionPage.objects.live()

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

        query_type = 'match'
        if operator == 'and':
            query_type = 'match_phrase'
        search = search.query(query_type, body=query_string)

        # Countries and categories may contain whitespace so don't join or
        # split on ' '.
        # Best approch is still to `try and see` rather than `checking`
        # https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
        try:
            countries = [wordify(i) for i in country_filters]
            if countries:
                search = search.filter('terms', country=countries)
        except TypeError:
            pass
        try:
            categories = [wordify(i) for i in category_filters]
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

        # Since we're going to `wordify` `category` & `country` to be useful as
        # filters, we need to add them to the `body` to be searchable as well.
        doc_body = '\n'.join([country, category, body])
        doc = {
            'country': wordify(country),
            'category': wordify(category),
            'body': doc_body,
            'parent_page_id': parent_page_id,
            'parent_page_type': parent_page_type,
            'content_id': content_id,
            'content_type': content_type,
        }
        result = self.es.index(index=self.es_index, doc_type=DOC_TYPE, body=doc,
                               id=content_id)
        return result.get('result') == 'created', result