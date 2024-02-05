from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from .forms import ShortLinkForm
from .models import ShortLink
import random
import string

class ShortLinkCreateView(CreateView):
    model = ShortLink
    form_class = ShortLinkForm
    template_name = 'urlShort/create_short_link.html'
    success_url = reverse_lazy('short_link_generated')

    def generate_short_code(self, number_of_characters=4):
        while True:
            short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(number_of_characters))
            if not ShortLink.objects.filter(short_code=short_code).exists():
                return short_code

    def form_valid(self, form):
        self.model.original_url = form.cleaned_data['original_url']
        short_code = self.generate_short_code()
        short_link = form.save(commit=False)
        short_link.short_code = short_code
        short_link.save()

        self.short_code = short_code  # to pass short_code to the success template
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('short_link_generated', kwargs={'short_code': self.short_code})
    
class RedirectOriginalView(View):
    def get(self, request, short_code):
        short_link = ShortLink.objects.get(short_code=short_code)
        return redirect(short_link.original_url)
    
class ShortLinkGeneratedView(View):
    template_name = 'urlShort/short_link_generated.html'
    def get(self, request, short_code, *args, **kwargs):
        return render(request, self.template_name, {'short_code': short_code})