from django.urls import path
from .views import ShortLinkCreateView, ShortLinkRedirectView, ShortLinkGeneratedView

urlpatterns = [
    path('', ShortLinkCreateView.as_view(), name='create_short_link'),
    path('short-link-generated/<str:short_code>/', ShortLinkGeneratedView.as_view(), name='short_link_generated'),
    path('<slug:short_code>/', ShortLinkRedirectView.as_view(), name='short_link_redirect'),
]
