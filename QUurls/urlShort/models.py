from django.db import models 
from django.utils.text import slugify
import random
import string

# Create your models here.

class ShortLink(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def clean_original_url(self):
        return 
    
    def clean_short_code(self,number_of_characters=4):
        while True:
            short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(number_of_characters))
            if not ShortLink.objects.filter(short_code=short_code).exists():
                return short_code
            
    def save(self, *args, **kwargs):
        self.slug = slugify(self.short_code)
        super().save(*args, **kwargs)
