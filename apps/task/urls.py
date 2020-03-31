from django.contrib import admin
from django.urls import path
from apps.task.views import TaskView, AddTaskView, TaskFinish, DeleteTask, deleteTask

urlpatterns = [
    path('task', TaskView.as_view(), name='task'),
    path('add_task', AddTaskView.as_view(), name='add task'),
    #path('task/<pk>', DeleteTask.as_view(), name='task_delete'),
    path('task/finish/<id_task>', TaskFinish, name='task_finish'),
     path('task/delete/<id_task>', deleteTask, name='task_delete'),
]
