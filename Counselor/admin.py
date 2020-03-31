from django.contrib import admin
from .models import CounselorProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
# class CounselorProfileInline(admin.StackedInline):
#     model = CounselorProfile
#     can_delete = False
#     verbose_name_plural = 'Counselor Profile'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (CounselorProfileInline,)
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
