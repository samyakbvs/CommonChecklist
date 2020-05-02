from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
from student.models import StudentProfile,Invite,Notes
from django.contrib.auth.models import User
import random
import string



# Create your views here.
class AllStudent(APIView):
    def get(self,request):
        current_user = request.user
        students  = current_user.counselorprofile.students.all()
        return render(request,'Checklist/students.html',{"students":students})
    def post(self,request):
        query = request.POST['query']
        return redirect("SearchStudent",query)

class Search(APIView):
    def get(self,request,query):
        current_user = request.user
        students  = current_user.counselorprofile.students.filter(name__contains=query)
        return render(request,'Checklist/students.html',{"students":students})

class AddNotes(APIView):
    def get(self,request,username):
        return render(request,'Checklist/addNotes.html',{'username':username})
    def post(self,request,username):
        user = User.objects.get(username=username)
        note = Notes(user=user,counselor_name=request.user.counselorprofile.name, text=request.POST['note'])
        note.save()
        return redirect('counselorHome')

class AddStudent(APIView):
    def get(self,request):
        return render(request,'Checklist/addStudents.html')
    def post(self,request):
        query = request.POST['query']
        return redirect("SearchAddStudent",query)

class SearchAddStudent(APIView):
    def get(self,request,query):
        # current_user = request.user
        students  =  StudentProfile.objects.filter(name__contains=query)
        return render(request,'Checklist/addStudents.html',{"students":students})

class InviteStudent(APIView):
    def get(self,request,stud):
        # student = StudentProfile.objects.get(name=stud)
        current_user = request.user
        student_user = User.objects.get(username=stud)
        print(stud)
        req = Invite(user=student_user,counselor_name = current_user.counselorprofile.name,token=self.randomString())

        req.save()

        return redirect('AccountCounselor')

    def randomString(self,stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

class CounselorHome(APIView):
    def get(self,request):
        return render(request,'Checklist/counHome.html')
