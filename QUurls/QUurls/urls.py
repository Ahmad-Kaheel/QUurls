from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlShort.urls')),
    path('file/', include('file_upload.urls')),
]

