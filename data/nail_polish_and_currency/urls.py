from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('', views.show_nail_polish, name='home'),
    path('price_update', views.crypto_price_update, name='update'),
    path('request', views.post_request, name='request'),
    path('live_broadcast/', views.live_broadcast, name='live_broadcast'),
]