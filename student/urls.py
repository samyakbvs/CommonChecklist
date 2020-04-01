from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('profile',views.ViewProfile.as_view(),name = "profile"),
path('viewessays', views.ViewEssay.as_view(), name = "viewEssay"),
path('addEssay', views.Essay.as_view(), name = "addEssay"),
path('studentHome', views.Home.as_view(), name = "studentHome"),
path('testing', views.Testing.as_view(), name = "testing"),
path('AddSatScore', views.AddSatScore.as_view(), name = "AddSatScore"),
path('AddActScore', views.AddActScore.as_view(), name = "AddActScore"),
path('AddSubjectScore', views.AddSubjectScore.as_view(), name = "AddSubjectScore"),
path('transcripts', views.Transcript.as_view(), name = "transcripts"),
path('lor', views.LOR.as_view(), name = "lor"),
path('activity', views.Activity.as_view(), name = "activity"),
path('changePassword', views.Password.as_view(), name = "changePassword")
]
