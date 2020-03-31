from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.contrib import auth
from Checklist.models import StudentProfile
from django.contrib.auth.forms import UserChangeForm
from .models import Essay
from django.contrib.auth.decorators import login_required

# Create your views here.
class ViewProfile(APIView):
    def get(self, request, user_id):
        prof = get_object_or_404(StudentProfile,pk=user_id)
        return render(request, 'student/profile.html', {"profile": prof})
class EditProfile(APIView):

    def get(self,request):
        form = UserChangeForm(instance=request.user)
        args = {'form':form}
        return render()

    def post(self,request):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            return redirect()

class Essay(APIView):

    def get(self,request):
        return render(request, 'student/essay.html')
    
    def post(self,request):
        if request.POST['name'] and request.POST['link'] and request.POST['date']:
            essay = Essay(user = request.user, link = request.POST['link'], name = request.POST['name'], date = request.POST['date'])
            essay.save()
