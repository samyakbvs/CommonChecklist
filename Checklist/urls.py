from django.contrib import admin
from django.urls import path,include
from . import views
from Counselor import urls as urlsCounselors
from student import urls as urlsStudents


urlpatterns = [
    path('',views.Home.as_view(),name="Home"),
    path('login/',views.Login.as_view(),name="Login"),
    path('signup/',views.Signup.as_view(),name="Signup"),
    path('counselor/',include(urlsCounselors)),
    path('student/',include(urlsStudents))
]
