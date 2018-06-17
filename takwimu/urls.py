from django.conf.urls import include, url
from django.conf.urls.static import static
from hurumap.urls import urlpatterns as hurumap_urlpatterns

from takwimu import settings
from takwimu.views import CountryReport, ContactUsPage

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              [url(r'^about/contact', ContactUsPage.as_view(), name='contact'), ] + \
              hurumap_urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns