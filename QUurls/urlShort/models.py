from django.db import models 
from django.utils.text import slugify

# Create your models here.

class ShortLink(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.short_code)
        super().save(*args, **kwargs)
