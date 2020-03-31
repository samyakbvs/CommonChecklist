from django.db import models
from django.contrib.auth.models import User
from Counselor.models import CounselorProfile
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Default name", max_length = 1000)
    school = models.CharField(max_length = 1000)
    boards = models.IntegerField()
    sat = models.IntegerField()
    act = models.IntegerField()
    counselor = models.ForeignKey(CounselorProfile, on_delete=models.CASCADE, null=True,related_name="students")

    def __str__(self):
        return self.name


class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 500)
    date = models.DateField()

    def __str__(self):
        return self.name
