from django.contrib import admin
from .models import *
# Register your models here.


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['__str__','course','position','slug', 'date_created',]
    search_fields = ['__str__', 'course']
    list_filter = ['course','position', 'date_created']
class CourseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'category','slug','date_created')
    search_fields = ('__str__', 'owner', 'category')
    list_filter = ('owner', 'category','date_created')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'chapter', 'position','date_created')
    search_fields =  ('__str__', 'chapter')
    list_filter = ('chapter', 'position','date_created')

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Competence)