from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail')
]
