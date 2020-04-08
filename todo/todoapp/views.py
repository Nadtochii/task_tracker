from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context=context)


def detail(request, task_id: int):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    context = {'task': task}
    return render(request, 'todoapp/detail.html', context=context)
