from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=254)
    birthday = models.DateField()

    def __str__(self):
        return self
