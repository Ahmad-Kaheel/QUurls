from django.forms import ModelForm
from .models import ShortLink

class ShortLinkForm(ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url']
