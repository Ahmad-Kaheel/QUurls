from django.contrib import admin

# Register your models here.

# urlShort/admin.py

from django.contrib import admin
from .models import ShortLink

# show the short code in the admin list
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code')
    
admin.site.register(ShortLink, ShortLinkAdmin)