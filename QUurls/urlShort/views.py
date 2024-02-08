from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, RedirectView
from .forms import ShortLinkForm
from .models import ShortLink


class ShortLinkCreateView(CreateView):
    template_name = 'urlShort/create_short_link.html'
    model = ShortLink
    form_class = ShortLinkForm


class ShortLinkRedirectView(RedirectView):
    pattern_name = None
    
    def get(self, request, short_code):
        short_link = ShortLink.objects.get(short_code=short_code)
        return redirect(short_link.original_url)

class ShortLinkGeneratedView(TemplateView):
    template_name = 'urlShort/short_link_generated.html'
