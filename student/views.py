from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.contrib import auth
from .models import StudentProfile
from django.contrib.auth.forms import UserChangeForm
from .models import Essay,StudentProfile, SAT, ACT, Activity,Invite, Transcript, SubjectTest, LOR
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Counselor.models import CounselorProfile


# Create your views here.
class Home(APIView):
    def get(self,request):
        profile = StudentProfile.objects.get(user = request.user)
        return render(request, 'student/studentHome.html',{"profile": profile})
class ChangePassword(APIView):
    def get(self,request):
        return render(request, 'student/changePassword.html')
    def post(self, request):
        user = User.objects.get(username = request.user)
        if user.check_password(request.POST['current']):
            if request.POST['new'] == request.POST['newVerify']:
                user.set_password(request.POST['new'])
                user.save()
                return redirect('studentHome')

            else:
                return render(request, 'student/changePassword.html', {"error":"Passwords don't match"})
        else:
            return render(request, 'student/changePassword.html', {"error":"Current Password is not correct"})
# class ViewProfile(APIView):
#     def get(self, request):
#         profile = StudentProfile.objects.get(user = request.user)
#         return render(request, 'student/profile.html', {"profile": profile})
#     def post(self,request):
#         profile = StudentProfile.objects.get(user = request.user)
#         profile.email = request.POST['email']
#         profile.name = request.POST['username']
#         profile.school = request.POST['school']
#         profile.save()
#         return redirect('studentHome')
class AddEssay(APIView):
    def get(self,request):
        return render(request, 'student/addEssay.html')
    def post(self,request):
        if request.POST['name'] and request.POST['link'] and request.POST['date']:
            essay = Essay(user = request.user, link = request.POST['link'], name = request.POST['name'], date = request.POST['date'])
            essay.save()
            return redirect('studentHome')
class ViewEssay(APIView):
    def get(self, request):
        try:
            essays = Essay.objects.all()
            return render(request, 'student/viewEssays.html',{"essays":essays})
        except:
            return render(request, 'student/viewEssays.html', {"error": "You Currently have no Essays"})
class ViewScores(APIView):
    def get(self, request):
        try:
            sat = SAT.objects.filter(user__username = request.user)
            try:
                scores = ACT.objects.filter(user__username = request.user)
                try:
                    subject = SubjectTest.objects.filter(user__username = request.user)
                    return render(request, 'student/viewScores.html', {"sat":sat, "scores":scores, "subject":subject})
                except:
                    return render(request, 'student/viewScores.html', {"sat":sat, "scores":scores} ,{"error":"No Subject Scores Uploaded yet"})
            except:
                try:
                    subject = SubjectTest.objects.filter(user__username = request.user)
                    return render(request, 'student/viewScores.html',{"sat":sat, "subject":subject, "error": "No ACT scores uploaded yet"})
                except:
                    return render(request, 'student/viewScores.html',{"sat":sat, "error": "No ACT and Subject Test scores uploaded yet"})
        except:
            try:
                scores = ACT.objects.filter(user__username = request.user)
                try:
                    subject = SubjectTest.objects.filter(user__username = request.user)
                    return render(request, 'student/viewScores.html', {"subject":subject, "scores":scores, "error":"No SAT scores uploaded yet"})
                except:
                    return render(request, 'student/viewScores.html', {"scores":scores, "error":"No Subject and SAT scores uploaded yet"})
            except:
                try:
                    subject = SubjectTest.objects.filter(user__username = request.user)
                    return render(request, 'student/viewScores.html', {"subject":subject, "error":"No SAT and ACT scores uploaded yet"})
                except:
                    return render(request, 'student/viewScores.html', {"error":"No scores uploaded yet"})

class Testing(APIView):
    def get(self, request):
        return render(request, 'student/addScores.html')
class AddSatScore(APIView):
    def get(self,request):
        try:
            scores = SAT.objects.filter(user__username = request.user)
            return render(request, 'student/addScores.html', {"tests": test})
        except:
            return render(request, 'student/addScores.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        sat = SAT(user = request.user, date = request.POST['date1'], transcripts = request.FILES.get('transcript1'))
        sat.save()
        return redirect('studentHome')
class AddActScore(APIView):
    def get(self,request):
        try:

            return render(request, 'student/addScores.html', {"tests": test})
        except:
            return render(request, 'student/addScores.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        act = ACT(user = request.user, date = request.POST['date2'], transcripts = request.FILES['transcript2'])
        act.save()
        return redirect('studentHome')
class AddSubjectScore(APIView):
    def get(self,request):
        try:

            return render(request, 'student/addScores.html', {"tests": test})
        except:
            return render(request, 'student/addScores.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        subject = SubjectTest(user = request.user, date = request.POST['date3'], transcripts = request.FILES['transcript3'])
        subject.save()
        return redirect('studentHome')
class ViewActivity(APIView):
    def get(self, request):
        try:
            activity = Activity.objects.filter(user__username = request.user)
            return render(request, 'student/viewActivity.html', {"activity":activity})
        except:
            return render(request, 'student/viewActivity.html', {"error":"No activities yet"})
class AddActivity(APIView):
    def get(self, request):
        return render(request, 'student/addActivity.html')
    def post(self,request):
        activity = Activity(user = request.user, name = request.POST['name'],category = request.POST['category'], grades = request.POST['grades'], position =request.POST['position'], hourperweek = request.POST['hoursperweek'], weeksperyear =request.POST['weeksperyear'], awards = request.POST['awards'], description = request.POST['description'])
        activity.save()
        return render(request, 'student/studentHome.html')
class ViewTranscript(APIView):
    def get(self,request):
        try:
            transcript = Transcript.objects.filter(user__username = request.user)
            return render(request, 'student/viewTranscripts.html', {"transcript": transcript})
        except:
            return render(request, 'student/viewTranscripts.html', {"error":"No transcripts uploaded yet"})
class AddTranscript(APIView):
    def get(self,request):
        return render(request, 'student/addTranscript.html')
    def post(self,request):
        transcript = Transcript(user = request.user, grade = request.POST['grade'], transcripts = request.FILES['transcript'])
        transcript.save()
        return render(request, 'student/studentHome.html')
class ViewLOR(APIView):
    def get(self,request):
        try:
            lor = LOR.objects.filter(user__username = request.user)
            return render(request, 'student/viewLOR.html', {"lor": lor})
        except:
            return render(request, 'student/viewLOR.html', {"error":"No transcripts uploaded yet"})
class AddLOR(APIView):
    def get(self, request):
        return render(request, 'student/addLOR.html')
    def post(self,request):
        lor = LOR(user = request.user, recommender = request.POST['recommender'], lor = request.FILES['transcript'])
        lor.save()
        return render(request, 'student/studentHome.html')

class CounselorInvite(APIView):
    def get(self,request):
        req = Invite.objects.filter(user=request.user)
        return render(request,'student/invite.html',{'req':req})

class AcceptInvite(APIView):
    def post(self,request,token):
        req = Invite.objects.get(token=token)
        current_user = request.user
        studentprofile = StudentProfile.objects.get(user=current_user)
        studentprofile.counselor = CounselorProfile.objects.get(name=req.counselor_name)
        print(studentprofile.counselor)
        studentprofile.save()
        return redirect('invitations')
