from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib import auth
# Create your views here.
class profile(APIView):
    def get(self,request):
        return render(request,'Counselor/account.html')

class addStudent(APIView):
    def get(self,request):
        return render(request,'Counselor/add.html')
