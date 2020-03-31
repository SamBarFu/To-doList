from django import forms
from apps.task.models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'user',
            'name_task',
            'description',
            'max_date',
        ]

        labels = {
            'user': 'user',
            'name_task': 'Task',
            'description': 'Description',
            'max_date': 'Date',
        }

        widgets = {
            'user': forms.Select(attrs={'class':'field'}),
            'name_task': forms.TextInput(attrs={'class':'field'}),
            'description': forms.TextInput(attrs={'class':'field'}),
            'max_date': forms.DateInput(attrs={'class':'field', 'type':'date'}),
        }