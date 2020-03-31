from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Task(models.Model):

    STATE = (
        ('C','Completed'),
        ('NC', 'Not Completed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_task = models.CharField(max_length=20)
    description = models.CharField(max_length=254)
    max_date = models.DateField()
    finish_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE, default='NC')

    def __str__(self):
        return self.name_task

    def dateNow(self):
        if date.today() > self.max_date:
            return 'style=color:crimson;'
        else:
            return 'style=color:black;'