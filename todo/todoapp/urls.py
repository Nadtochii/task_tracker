from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import TaskViewSet

app_name = 'todoapp'

router = routers.SimpleRouter()
router.register('', TaskViewSet)


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^', include(router.urls)),
]
