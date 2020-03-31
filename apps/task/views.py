from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from datetime import datetime

from apps.task.forms import TaskForm
from apps.task.models import Task

# Create your views here.
class TaskView(ListView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'tasks'
   

class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('task')

class UpdateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('task')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('task')

def TaskFinish(request, id_task):
    task = Task.objects.get(id=id_task)
    task.finish_date = datetime.now()
    task.state = 'C'
    task.save()
    return redirect('task')
  
def deleteTask(request, id_task):
    task = Task.objects.get(id=id_task)
    print(1)
    task.delete()
    return redirect('task')