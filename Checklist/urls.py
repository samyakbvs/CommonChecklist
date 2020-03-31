from django.contrib import admin
from django.urls import path,include
from . import views
from Counselor import urls as urlsCounselors
from student import urls as urlsStudents


urlpatterns = [
    path('',views.home.as_view(),name="Home"),
    path('login/',views.login.as_view(),name="Login"),
    path('signup/',views.signup.as_view(),name="Signup"),
    path('account/',include(urlsCounselors)),
    path('student/',include(urlsStudents))
]
