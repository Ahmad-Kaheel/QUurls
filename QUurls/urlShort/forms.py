from django import forms
from .models import ShortLink
from django.core.exceptions import ValidationError

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url','short_code']


class ContactForm(forms.Form):
    def clean_recipients(self):
        short_code = self.cleaned_data["short_code"]
        if not short_code:
            raise ValidationError("Empty original_url")
        return short_code

class ShortLinkFormMixin():
    # def generate_short_code(self, number_of_characters=4):
    #     while True:
    #         short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(number_of_characters))
    #         if not ShortLink.objects.filter(short_code=short_code).exists():
    #             return short_code
    
    def form_valid(self, form):
        self.model.original_url = form.cleaned_data['original_url']
        short_code = self.generate_short_code()
        short_link = form.save(commit=False)
        short_link.short_code = short_code
        short_link.save()
        
        self.short_code = short_code  # to pass short_code to the success template
        return super().form_valid(form)
