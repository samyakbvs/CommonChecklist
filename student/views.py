from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.contrib import auth
from .models import StudentProfile
from django.contrib.auth.forms import UserChangeForm
# from .models import Essay,StudentProfile, SAT, ACT, Activity,Invite, Transcript, SubjectTest, LOR
from .models import Essay,StudentProfile, Activity,Invite, Transcript, Testing, LOR
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Counselor.models import CounselorProfile
from datetime import datetime

# Create your views here.
class Home(APIView):
    def get(self,request):
        profile = StudentProfile.objects.get(user = request.user)
        return render(request, 'Checklist/studHome.html',{"profile": profile})


class AddEssay(APIView):
    def get(self,request):
        return render(request, 'Checklist/addEssay.html')
    def post(self,request):

        if request.POST['name'] and str(request.POST['link']):
            print("baba")
            essay = Essay(user = request.user, link = str(request.POST['link']), name = request.POST['name'], date = datetime.today().strftime('%Y-%m-%d'))
            essay.save()
            return redirect('studentHome')
        else:
            return render(request, 'Checklist/addEssay.html')

class ViewEssay(APIView):
    def get(self, request):
        try:
            essays = Essay.objects.filter(user=request.user)
            return render(request, 'Checklist/viewEssays.html',{"essays":essays})
        except:
            return render(request, 'Checklist/viewEssays.html', {"error": "You Currently have no Essays"})

class AddTesting(APIView):
    def get(self, request):
        return render(request, 'Checklist/addScores.html')
    def post(self,request):
        test = Testing(user=request.user,type=request.POST['type'],date=request.POST['date'],transcripts = request.FILES['transcript'])
        test.save()
        return redirect('studentHome')
class ViewTesting(APIView):
    def get(self,request):
        tests = Testing.objects.filter(user=request.user)
        return render(request, 'Checklist/viewScores.html', {"tests":tests})
    def post(self,request):
        pass
class ViewActivity(APIView):
    def get(self, request):
        try:
            activity = Activity.objects.filter(user = request.user)
            return render(request, 'Checklist/viewActivity.html', {"activity":activity})
        except:
            return render(request, 'Checklist/viewActivity.html', {"error":"No activities yet"})
class AddActivity(APIView):
    def get(self, request):
        return render(request, 'Checklist/addActivity.html')
    def post(self,request):
        activity = Activity(user = request.user, category = request.POST['category'], grades = request.POST['grades'], position =request.POST['position'], hourperweek = request.POST['hoursperweek'], weeksperyear =request.POST['weeksperyear'], awards = request.POST['awards'], description = request.POST['description'])
        activity.save()
        return redirect('studentHome')
class ViewTranscript(APIView):
    def get(self,request):
        try:
            transcript = Transcript.objects.filter(user = request.user)
            return render(request, 'Checklist/viewTranscripts.html', {"transcript": transcript})
        except:
            return render(request, 'Checklist/viewTranscripts.html', {"error":"No transcripts uploaded yet"})
class AddTranscript(APIView):
    def get(self,request):
        return render(request, 'Checklist/addTranscript.html')
    def post(self,request):
        transcript = Transcript(user = request.user, grade = request.POST['grade'], transcripts = request.FILES['transcript'])
        transcript.save()
        return redirect('studentHome')
class ViewLOR(APIView):
    def get(self,request):
        try:
            lor = LOR.objects.filter(user = request.user)
            return render(request, 'Checklist/viewLetter.html', {"lor": lor})
        except:
            return render(request, 'Checklist/viewLetter.html', {"error":"No transcripts uploaded yet"})
class AddLOR(APIView):
    def get(self, request):
        return render(request, 'Checklist/addLetter.html')
    def post(self,request):
        lor = LOR(user = request.user, recommender = request.POST['recommender'],email=request.POST['email'],post=request.POST['post'], lor = request.FILES['transcript'])
        lor.save()
        return redirect('studentHome')

class CounselorInvite(APIView):
    def get(self,request):
        req = Invite.objects.filter(user=request.user)
        return render(request,'Checklist/invite.html',{'req':req})

class AcceptInvite(APIView):
    def get(self,request,token):
        req = Invite.objects.get(token=token)
        current_user = request.user
        studentprofile = StudentProfile.objects.get(user=current_user)
        studentprofile.counselor = CounselorProfile.objects.get(name=req.counselor_name)

        studentprofile.save()
        req.delete()
        return redirect('invitations')

class DeclineInvite(APIView):
    def get(self,request,token):
        req = Invite.objects.get(token=token)
        req.delete()
        return redirect('invitations')

class Profile(APIView):
    def get(self,request,username):
        profile_user = User.objects.get(username=username)
        testing = Testing.objects.filter(user = request.user)
        essays = Essay.objects.filter(user = request.user)
        activities = Activity.objects.filter(user = request.user)
        lors = LOR.objects.filter(user = request.user)
        transcripts = Transcript.objects.filter(user = request.user)
        return render(request, "Checklist/profile.html",{'profile_user':profile_user, 'testing': testing, 'essays':essays, 'activities':activities, 'lors':lors, 'transcripts':transcripts})
