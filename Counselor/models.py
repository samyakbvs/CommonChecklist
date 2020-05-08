from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CounselorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Default name", max_length = 1000)

    def __str__(self):
        return self.name
class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 500, null = True)
    link = models.URLField(max_length = 1000)
    link2 = models.URLField(max_length = 1000, null = True)
