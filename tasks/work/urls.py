from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_home, name='work_home'),
    path('closed/', views.work_closed, name='work_closed'),
    path('<int:pk>', views.WorktaskDetailView.as_view(), name='task-descr'),
    path('create_task', views.create_task, name='create_task'),
]
