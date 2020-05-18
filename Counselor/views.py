from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
from student.models import StudentProfile,Invite,Notes, Activity
from Counselor.models import Link
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
        students  = current_user.counselorprofile.students.filter(name__icontains=query)
        return render(request,'Checklist/students.html',{"students":students})
class ViewActivity(APIView):
    def get(self,request, username):
        activity = Activity.objects.filter(user__username = username)
        profile_user = User.objects.get(username=username)
        return render(request, 'Checklist/counviewact.html', {"activity":activity, "profile_user": profile_user})
class AddNotes(APIView):
    def get(self,request):
        return render(request,'Checklist/addNotes.html')
    def post(self,request):
        user = User.objects.get(username=request.POST['username'])
        note = Notes(user=user,counselor_name=request.user.counselorprofile.name, text=request.POST['note'])
        note.save()
        prof = StudentProfile.objects.get(user = user)
        prof.newmessage = True
        prof.save()
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
        students  =  StudentProfile.objects.filter(name__icontains=query)
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
class AddLink(APIView):
    def get(self,request):
        return render(request, 'Checklist/counLink.html')
    def post(self,request):
        link = Link(user = request.user, title = request.POST['title'], link = request.POST['link'], link2 = request.POST['link2'])
        link.save()
        return redirect('counselorHome')
def delete(request, model, model_id):
    id =  int(model_id)
    my_model = getattr(models,model)
    instance = get_object_or_404(my_model,pk = model_id)
    instance.delete()
    return rendirect('counselorHome')
