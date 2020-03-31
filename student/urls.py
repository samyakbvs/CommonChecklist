from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('profile/<int:user_id>',views.ViewProfile.as_view(),name = "profile"),
path('editprofile', views.EditProfile.as_view(), name = "edit"),
path('addEssay', views.Essay.as_view(), name = "addEssay")

]
