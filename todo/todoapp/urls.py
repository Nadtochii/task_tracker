from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail')
]
