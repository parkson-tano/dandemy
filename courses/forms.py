from django import forms
from django.contrib.auth.models import User
from .models import Course, Chapter, Lesson, Category

class CategoryForm(forms.Form):
    class Meta:
        models = Category
        field = "__all__"
        # help_text = {
        #     'title': 'Ex. Introduction to Programming or Biology',
        #     'description': 'Short description about course',
        #     'image': 'Upload a Course photo or leave it blank',
        #     'category': 'select best category for this class',
        # }

class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = "__all__"
        # help_text = {
        #     'title': 'Ex. Variable or Reproduction',
        #     'description': 'Short description about subject',
        #     'course': 'select course of subject',
        #     'subject_image': 'Upload a Course photo or leave it blank',
        # }

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = "__all__"

class LessonForm(forms.Form):
    class Meta:
        models = Lesson
        fields = "__all__"

        # help_text = {
        #     'title': 'Lesson Title',
        #     'chapter': 'Select subject for the lesson',
        #     'video_id': 'Enter the video ID from Youtube to upload (<a href="/media/youtube_help.png"> where can i find the ID </a>)',
        #     'video': 'upload lesson video',
        #     'position': 'Enter the position of lesson',
        # }