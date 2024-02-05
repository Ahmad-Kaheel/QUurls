from django.urls import path
from .views import ShortLinkCreateView, RedirectOriginalView, ShortLinkGeneratedView

urlpatterns = [
    path('', ShortLinkCreateView.as_view(), name='create_short_link'),
    path('short-link-generated/<str:short_code>/', ShortLinkGeneratedView.as_view(), name='short_link_generated'),
    path('<str:short_code>/', RedirectOriginalView.as_view(), name='redirect_to_original'),
]
