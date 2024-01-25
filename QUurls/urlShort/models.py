from django.db import models

# Create your models here.

class ShortLink(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=4, unique=True)