from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, View, CreateView,FormView
from .models import Course, Chapter, Lesson
from category.models import Category, SubCategory
from .forms import *
from django.db.models import Q
from itertools import chain
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course= Course.objects.all()
        context["course"] = course
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        category = Category.objects.get(id = url_slug)
        course = Course.objects.filter(category=url_slug)
        context['category'] = category
        context["course"] = course
        return context
    
class CourseListView(ListView):
    template_name = 'course/course_list.html'
    model = Course
    context_object_name = 'courses'
    
class CourseDetailView(TemplateView):
    template_name = "course/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        course = Course.objects.get(slug=url_slug)
        chapter = Chapter.objects.filter(course=course).order_by('position')
        context['chapter'] = chapter
        return context

class ChapterDetailView(TemplateView):
    template_name = 'chapter_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        chapter = Chapter.objects.get(slug=url_slug)
        lesson = Lesson.objects.filter(chapter=chapter).order_by('position')
        context["chapter"] = chapter
        context['lesson'] = lesson 
        return context

class LessonDetailView(View):
    def get(self, request, chapter_slug, lesson_slug, *args, **kwargs):
        chapter = get_object_or_404(Chapter, slug=chapter_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)  
        context = {'lesson' : lesson}
        return render(request, 'course/lesson_detail.html', context)

class SearchView(TemplateView):
    template_name = 'course/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        course = Course.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
        chapter = Chapter.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
        lesson = Lesson.objects.filter(Q(title__icontains=kw))
        result = chain(course, lesson, chapter)
        context["result"] = result
        return context
    
class CreateChapterView(FormView):
    template_name = 'course/create_chapter.html'
    form_class = ChapterForm
    success_url = ''

class CreateCourseView(FormView):
    template_name = 'course/create_course.html'
    form_class = CourseForm
    success_url = ''

class CreateLessonView(FormView):
    template_name = 'course/create_lesson.html'
    form_class = LessonForm
    success_url = ''