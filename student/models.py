from django.db import models
from django.contrib.auth.models import User
from Counselor.models import CounselorProfile
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Default name", max_length = 1000)
    school = models.CharField(max_length = 1000)
    counselor = models.ForeignKey(CounselorProfile, on_delete=models.CASCADE, null=True,related_name="students")
    def __str__(self):
        return self.name
class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 500)
    date = models.DateField()
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 500)
    category = models.CharField(max_length = 500)
    grades = models.CharField(max_length = 100)
    position = models.CharField(max_length = 300)
    hourperweek = models.IntegerField()
    weeksperyear = models.IntegerField()
    awards = models.CharField(max_length = 500)
    description = models.CharField(max_length = 200)
class SAT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    transcripts = models.FileField(upload_to = 'sat/')
class ACT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    transcripts = models.FileField(upload_to = 'act/')
class SubjectTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length = 50)
    transcripts = models.FileField(upload_to = 'sat2/')
class Transcript(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length = 50)
    transcripts = models.FileField(upload_to= 'transcripts/')
class LOR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommender = models.CharField(max_length = 200)
    lor = models.FileField(upload_to = 'lor/')
class Invite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counselor_name = models.CharField(max_length = 200)
    token = models.CharField(max_length = 11)
