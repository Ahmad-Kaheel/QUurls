from django.urls import path
from .views import create_short_link, redirect_to_original

urlpatterns  = [
    path('', create_short_link, name='create_short_link'),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
]