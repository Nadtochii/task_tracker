from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Task
from .serializers import TaskSerializer


class IndexView(ListView):
    model = Task
    template_name = 'todoapp/index.html'


class TaskViewSet(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    template_name = 'todoapp/detail.html'
