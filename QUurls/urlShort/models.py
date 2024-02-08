from django.shortcuts import reverse
from django.db.models import (
    Model,
    URLField,
    CharField,
    SlugField,
)

import random
import string


class ShortLink(Model):
    original_url = URLField()
    short_code = SlugField(unique=True, max_length=4)
    
    def get_short_code(self,number_of_characters=4):
        while True:
            short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(number_of_characters))
            if not ShortLink.objects.filter(short_code=short_code).exists():
                return short_code

    def save(self, *args, **kwargs):
        self.short_code = self.get_short_code()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('short_link_generated', kwargs={'short_code': self.short_code})
