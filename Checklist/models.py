from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Default name", max_length = 1000)
    school = models.CharField(max_length = 1000)
    boards = models.IntegerField()
    sat = models.IntegerField()
    act = models.IntegerField()
