import json
import requests

from collections import OrderedDict
from django.conf import settings
from django.core.serializers import serialize
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView, FormView, View
from django.views.generic.base import TemplateView
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query

from takwimu.models.dashboard import ExplainerSteps, FAQ, Testimonial, \
    TopicPage, ProfileSectionPage, ProfilePage
from forms import SupportServicesContactForm


class HomePageView(TemplateView):
    """
    Home Page View:
    ---------------
    View of homepage.
    """
    template_name = 'takwimu/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['explainer_steps'] = ExplainerSteps.objects.first()
        context['faqs'] = FAQ.objects.all()
        context['testimonials'] = Testimonial.objects.all().order_by('-id')[:3]
        return context


class AboutUsView(TemplateView):
    template_name = 'takwimu/about/index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        return context


class LegalView(TemplateView):
    """
    Legal View:
    ---------------
    View of legal notices: Terms of Use, Privacy and Cookie policies.
    """
    template_name = 'takwimu/about/legal.html'


class TopicView(TemplateView):
    """
    Topic View:
    ---------------
    Finding Data by Topic View.
    """
    template_name = 'takwimu/topic_page.html'


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


class SupportServicesIndexView(FormView):
    """
    Support Services View
    --------------------
    View of support services page.
    """
    template_name = 'takwimu/about/support_services.html'
    form_class = SupportServicesContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SupportServicesIndexView, self).get_context_data(
            **kwargs)
        context['ticket_success'] = False
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        location = form.cleaned_data['location']
        role = form.cleaned_data['role']
        help_wanted = form.cleaned_data['help']
        print '\n\n\n\n\n\n\n\n'
        data = {
            'request': {
                'requester': {
                    "name": name,
                    "email": email
                },
                'subject': 'Enquiry: {} a(n) {} from {} asks'.format(name, role,
                                                                     location),
                'comment': {
                    'body': help_wanted
                }
            }
        }

        headers = {'content-type': 'application/json'}

        user = email + '/token'
        api_token = settings.ZENDESK_API_TOKEN

        request = requests.post(
            settings.ZENDESK_API,
            data=json.dumps(data),
            auth=(user, api_token),
            headers=headers
        )

        print '\n\n\n\n\n\n\n\n'
        print request.status_code
        print request.json()

        if request.status_code != 201:
            # add non field error
            form.add_error(None,
                           'Could not open a ticket at the moment. Please try again later')
            return super(SupportServicesIndexView, self).form_invalid(form)

        context = self.get_context_data(form=form)
        # hide form and show the success dialog
        context['ticket_success'] = True
        return self.render_to_response(context)

    def form_invalid(self, form):
        print('\n\n\n\n\n\n')
        print form.data
        return super(SupportServicesIndexView, self).form_invalid(form)


class SearchView(TemplateView):
    """
    Search View
    -----------
    Displays search results.

    """
    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        self.items = []
        self.countries = OrderedDict()
        self.topics = OrderedDict()
        if search_query:

            # Profile page only indexes geo and body but not sections.
            profilepage_results = ProfilePage.objects.live().search(
                search_query)
            for profilepage in profilepage_results.results():
                self._extract_search_results(request, profilepage)

            # Hence, sections (i.e. topics in the UI) need to be searched independent
            # of profile page
            profilesectionpage_results = ProfileSectionPage.objects.live().search(search_query)
            for profilesectionpage in profilesectionpage_results.results():
                self._extract_search_results(request, profilesectionpage)

            Query.get(search_query).add_hit()
        return render(request, self.template_name, {
            'search_query': search_query,
            'search_results': {
                'items': self.items,
                'countries': self.countries.keys(),
                'topics': self.topics.keys(),
            },
        })

    def _extract_search_results(self, request, page):
        (country, category) = (str(page.get_parent()), page.title) \
            if isinstance(page, ProfileSectionPage) \
            else (str(page), u'Country Overview')
        self.countries[country] = 1
        self.topics[category] = 1
        url = page.get_url(request)
        for topic in page.body:
            result = {
                'country': country,
                'region': 'National',
                'category': category,
                'url': url,
                'data_point': topic,
            }
            self.items.append(result)
