from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('counselorHome',views.CounselorHome.as_view(),name="counselorHome"),
    path('allStudents',views.AllStudent.as_view(),name="AccountCounselor"),
    path('addStudent', views.AddStudent.as_view(), name="AddStudents"),
    path('addNotes/<str:username>', views.AddNotes.as_view(), name = "addNotes"),
    path('searchStudent/<str:query>', views.Search.as_view(), name="SearchStudent"),
    path('searchAddStudent/<str:query>', views.SearchAddStudent.as_view(), name="SearchAddStudent"),
    path('invite/<str:stud>', views.InviteStudent.as_view(), name="Invite")

]
