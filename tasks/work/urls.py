from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_home, name='work_home'),

]
