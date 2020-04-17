from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView

from .models import Task


class IndexView(ListView):
    model = Task
    template_name = 'todoapp/index.html'


class TaskView(DetailView):
    model = Task
    template_name = 'todoapp/detail.html'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/todoapp/'


def create_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        Task.objects.create(name=name, priority=priority, description=description)

        return redirect('/todoapp/')
