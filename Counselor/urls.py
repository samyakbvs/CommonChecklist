from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('students',views.profile.as_view(),name="AccountCounselor"),
    path('addStudent', views.addStudent.as_view(), name="AddStudents"),
]
