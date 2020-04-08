from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('counselorHome',views.CounselorHome.as_view(),name="counselorHome"),
    path('allStudents',views.AllStudent.as_view(),name="AccountCounselor"),
    path('addStudent', views.AddStudent.as_view(), name="AddStudents"),
    path('searchStudent/<slug:query>', views.Search.as_view(), name="SearchStudent"),
    path('searchAddStudent/<slug:query>', views.SearchAddStudent.as_view(), name="SearchAddStudent"),
    path('invite/<slug:stud>', views.InviteStudent.as_view(), name="Invite")

]
