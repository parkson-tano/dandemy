from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('category/<slug:slug>', CategoryView.as_view(), name='category_detail'),
    path('chapter/<slug:slug>', ChapterDetailView.as_view(), name='chapter_detail'),
    path('course', CourseListView.as_view(), name='course'),
    path('course/<slug:slug>', CourseDetailView.as_view(), name='course_detail'),
    path('lesson/<chapter_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('create/class/', CreateChapterView.as_view(), name='create_chapter'),
    path('create/course/', CreateCourseView.as_view(), name='create_course'),
    path('create/lesson/', CreateLessonView.as_view(), name='create_lesson'),
]