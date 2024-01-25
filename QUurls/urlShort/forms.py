from django import forms

class ShortLinkForm(forms.Form):
    original_url = forms.URLField(label='Original URL')