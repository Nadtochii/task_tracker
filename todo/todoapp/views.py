from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Task


class IndexView(ListView):
    model = Task
    template_name = 'todoapp/index.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todoapp/detail.html'
