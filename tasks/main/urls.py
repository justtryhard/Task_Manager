from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lgt', views.logging_out, name='lgt'),
    path('create_adv', views.create_adv, name='create_adv'),
]
