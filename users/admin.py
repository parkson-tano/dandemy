from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TeacherProfile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','is_teacher')

admin.site.register(Profile, ProfileAdmin)
