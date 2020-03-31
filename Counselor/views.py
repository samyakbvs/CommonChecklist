from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
# Create your views here.
class profile(APIView):
    def get(self,request):
        current_user = request.user
        students  = current_user.counselorprofile.students.all()
        return render(request,'Counselor/account.html',{"students":students})
    def post(self,request):
        query = request.POST['query']
        return redirect("SearchStudent",query)

class Search(APIView):
    def get(self,request,query):
        current_user = request.user
        students  = current_user.counselorprofile.students.filter(name__contains=query)
        return render(request,'Counselor/account.html',{"students":students})

class addStudent(APIView):
    def get(self,request):
        return render(request,'Counselor/add.html')
