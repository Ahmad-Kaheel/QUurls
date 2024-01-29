# file_upload/urls.py

from django.urls import path
from .views import upload_file, view_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('file/<str:signed_value>/', view_file, name='view_file'),
]