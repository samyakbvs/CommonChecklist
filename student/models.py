from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Essay(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 500)
    date = models.DateField()
