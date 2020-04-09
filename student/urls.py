from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
# path('profile',views.ViewProfile.as_view(),name = "profile"),
path('viewEssays', views.ViewEssay.as_view(), name = "viewEssay"),
path('addEssay', views.AddEssay.as_view(), name = "addEssay"),
path('studentHome', views.Home.as_view(), name = "studentHome"),
path('profile/<str:username>', views.Profile.as_view(), name = "profile"),
path('addTesting', views.AddTesting.as_view(), name = "addTesting"),
path('viewTranscripts', views.ViewTranscript.as_view(), name = "viewTranscripts"),
path('addTranscript',views.AddTranscript.as_view(), name = "addTranscript"),
path('viewLOR', views.ViewLOR.as_view(), name = "viewLOR"),
path('addLOR', views.AddLOR.as_view(), name = "addLOR"),
path('viewActivity', views.ViewActivity.as_view(), name = "viewActivity"),
path('addActivity', views.AddActivity.as_view(), name = "addActivity"),
path('changePassword', views.ChangePassword.as_view(), name = "changePassword"),
path('viewTesting', views.ViewTesting.as_view(), name= "viewTesting"),
path('invitations',views.CounselorInvite.as_view(), name='invitations'),
path('acceptInvitation/<str:token>',views.AcceptInvite.as_view(), name='acceptInvitation'),
path('declineInvitation/<str:token>',views.DeclineInvite.as_view(), name='declineInvitation')
]
