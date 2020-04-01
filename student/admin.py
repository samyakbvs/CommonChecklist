from django.contrib import admin
from .models import Essay,StudentProfile, SAT, ACT, Activity, Transcript, SubjectTest, LOR
from Counselor.models import CounselorProfile
# Register your models here.
# admin.site.register(Essay)
# admin.site.register(StudentProfile)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'StudentProfiles'

class CounselorProfileInline(admin.StackedInline):
    model = CounselorProfile
    can_delete = False
    verbose_name_plural = 'Counselor Profile'

class EssaysInline(admin.StackedInline):
    model = Essay
    can_delete = False
    verbose_name_plural = 'Essays'
class UserAdmin(BaseUserAdmin):
    inlines = (StudentProfileInline,EssaysInline,CounselorProfileInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(SAT)
admin.site.register(ACT)
admin.site.register(SubjectTest)
admin.site.register(Activity)
admin.site.register(Transcript)
admin.site.register(LOR)
