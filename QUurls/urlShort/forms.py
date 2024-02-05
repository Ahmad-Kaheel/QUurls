from django import forms
from .models import ShortLink

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url','short_code']
