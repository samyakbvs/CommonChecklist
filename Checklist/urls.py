from django.contrib import admin
from django.urls import path,include
from . import views
from Counselor import urls as urlsCounselors
from student import urls as urlsStudents


urlpatterns = [
    path('',views.Login.as_view(),name="Login"),
    path('signup/',views.Signup.as_view(),name="Signup"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('counselor/',include(urlsCounselors)),
    path('changePassword', views.ChangePassword.as_view(), name = "changePassword"),
    path('student/',include(urlsStudents)),

]
