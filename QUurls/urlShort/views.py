from typing import Any
from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from .forms import ShortLinkForm, ShortLinkFormMixin
from .models import ShortLink
import random
import string

class ShortLinkCreateView(CreateView, ShortLinkFormMixin):
    model = ShortLink
    form_class = ShortLinkForm
    template_name = 'urlShort/create_short_link.html'
    success_url = reverse_lazy('short_link_generated')
    
    def get_success_url(self):
        return reverse('short_link_generated', kwargs={'short_code': self.short_code})

class ShortLinkRedirectView(View):
    def get(self, request, short_code):
        short_link = ShortLink.objects.get(short_code=short_code)
        return redirect(short_link.original_url)

class ShortLinkGeneratedView(View):
    template_name = 'urlShort/short_link_generated.html'
    def get(self, request, short_code, *args, **kwargs):
        return render(request, self.template_name, {'short_code': short_code})