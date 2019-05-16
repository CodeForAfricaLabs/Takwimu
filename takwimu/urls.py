from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from wagtail.api.v2.router import WagtailAPIRouter

from takwimu import settings
from takwimu.views import HomePageView, LegalView, \
    IndicatorsGeographyDetailView, SearchAPIView, AutoCompleteAPIView, \
        AboutPageRedirectView
from wazimap.views import HomepageView as ProfileView
from takwimu.views import handler404, handler500
from takwimu.feed import CountryProfileFeed
from hurumap.dashboard.urls import urlpatterns as hurumap_dashboard_urlpatterns
from .api import api_router

GEOGRAPHY_LEVELS = '|'.join(settings.WAZIMAP['levels'].keys())
PROFILES_GEOGRAPHY_REGEX = r'profiles/(?P<geography_id>[{}]+-\w+)(-(?P<slug>[\w-]+))?'.format(
    GEOGRAPHY_LEVELS)


takwimu_urlpatterns = [
    url(r'^$', cache_page(60 * 60)(HomePageView.as_view()), name='home'),
    url(r'^faqs$', AboutPageRedirectView.as_view(), name='faqs'),
    url(r'^services$', AboutPageRedirectView.as_view(), name='services'),
    url(r'^methodology$', AboutPageRedirectView.as_view(), name='methodology'),
    url(r'^legal$', LegalView.as_view(), name='legal'),
    url(
        r'^{}/$'.format(PROFILES_GEOGRAPHY_REGEX),
        IndicatorsGeographyDetailView.as_view(),
        name='geography_detail'),
    url(r'^profiles/$', ProfileView.as_view(), name='profiles'),
    url(r'^feed/$', CountryProfileFeed(), name='rss_feed'),
    url(r'^api/search/$', SearchAPIView.as_view(), name='api-search'),
    url(r'^api/autocomplete/$', AutoCompleteAPIView.as_view(),
        name='api-autocomplete'),
    url(r'^api/v2/', api_router.urls),
]

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    takwimu_urlpatterns + hurumap_dashboard_urlpatterns

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^404/$', handler404, name='error_404'),
        url(r'^500/$', handler500, name='error_500'),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

handler404 = 'takwimu.views.handler404'
handler500 = 'takwimu.views.handler500'
