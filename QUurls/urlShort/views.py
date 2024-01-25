from django.shortcuts import render, redirect
from .forms import ShortLinkForm
from .models import ShortLink
import random
import string


def generate_short_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))

def create_short_link(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_code = generate_short_code()
            
            short_link = ShortLink(original_url=original_url, short_code=short_code)
            short_link.save()

            return render(request, 'urlShort/short_link_generated.html', {'short_code': short_code})
    else:
        form = ShortLinkForm()

    return render(request, 'urlShort/create_short_link.html', {'form': form})

def redirect_to_original(request, short_code):
    short_link = ShortLink.objects.get(short_code=short_code)
    return redirect(short_link.original_url)