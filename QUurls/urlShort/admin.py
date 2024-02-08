from django.contrib import admin

# Register your models here.

# urlShort/admin.py

from django.contrib import admin
from .models import ShortLink


class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code')
    
admin.site.register(ShortLink, ShortLinkAdmin)