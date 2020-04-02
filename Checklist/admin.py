from django.contrib import admin
from student.models import Essay,StudentProfile, SAT, ACT, Activity,Invite, Transcript, SubjectTest, LOR

from Counselor.models import CounselorProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class StudentProfileInline(admin.TabularInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'StudentProfiles'

class CounselorProfileInline(admin.TabularInline):
    model = CounselorProfile
    can_delete = False
    verbose_name_plural = 'Counselor Profiles'

class EssaysInline(admin.TabularInline):
    model = Essay
    can_delete = False
    verbose_name_plural = 'Essays'

class SATInline(admin.TabularInline):
    model = SAT
    can_delete = False
    verbose_name_plural = 'SATs'

class ACTInline(admin.TabularInline):
    model = ACT
    can_delete = False
    verbose_name_plural = 'ACTs'

class SubjectTestInline(admin.TabularInline):
    model = SubjectTest
    can_delete = False
    verbose_name_plural = 'SubjectTests'

class ActivityInline(admin.TabularInline):
    model = Activity
    can_delete = False
    verbose_name_plural = 'Activities'

class TranscriptInline(admin.TabularInline):
    model = Transcript
    can_delete = False
    verbose_name_plural = 'Transcripts'

class LORInline(admin.TabularInline):
    model = LOR
    can_delete = False
    verbose_name_plural = 'LORs'

class InviteInline(admin.TabularInline):
    model = Invite
    can_delete = False
    verbose_name_plural = 'Invites'

class UserAdmin(BaseUserAdmin):
    inlines = (StudentProfileInline,CounselorProfileInline,EssaysInline,SATInline,ACTInline,SubjectTestInline,TranscriptInline,LORInline,InviteInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
