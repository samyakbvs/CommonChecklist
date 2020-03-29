from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name="Home"),
    path('login/',views.login.as_view(),name="Login"),
    path('signup/',views.signup.as_view(),name="Signup"),
    path('account/',views.account.as_view(),name="Account")
]
