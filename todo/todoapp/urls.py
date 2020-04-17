from django.urls import path

from . import views

app_name = 'todoapp'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'<int:pk>/', views.TaskView.as_view()),
    path(r'<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
    path(r'create/', views.create_task),
]
