from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from student.models import StudentProfile
# Create your views here.
class Home(APIView):
    def get(self,request):
        return render(request,'Checklist/homepage.html')

class Signup(APIView):
    def get(self,request):
        return render(request,'Checklist/signup.html')
    def post(self,request):
        if request.POST['password'] == request.POST['verifyPassword']:
            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'Checklist/signup.html', {"error": "Valid email Id please"})
            try:
                email = StudentProfile.objects.get(request.POST['email'])
                return render(request, 'Checklist/signup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'Checklist/signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password'])
                profile = StudentProfile(user = user, email = request.POST['email'], name = request.POST['name'], school= request.POST['school'])
                profile.save()
                return render(request, 'student/studentHome.html')
        else:
            return render(request, 'Checklist/signup.html', {'error':'Passwords dont match'})
class Login(APIView):
    def get(self,request):
        return render(request,'Checklist/login.html')
    def post(self,request):
        user = auth.authenticate(username=request.POST['Username'],password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('AccountCounselor')
            else:
                return redirect('studentHome')
        return redirect('Login')
