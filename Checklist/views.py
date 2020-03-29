from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
# Create your views here.
class home(APIView):
    def get(self,request):
        return render(request,'Checklist/homepage.html')

class signup(APIView):
    def get(self,request):
        return render(request,'Checklist/signup.html')

class login(APIView):
    def get(self,request):
        return render(request,'Checklist/login.html')
    def post(self,request):
        user = auth.authenticate(username=request.POST['Username'],password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            return redirect('Account')
        return redirect('Login')

class account(APIView):
    def get(self,request):
        return render(request,'Checklist/account.html')
