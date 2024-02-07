from django import forms
from .models import ShortLink
import random
import string

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url','short_code']

class ShortLinkFormMixin():
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
