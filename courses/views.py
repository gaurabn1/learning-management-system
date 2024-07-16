from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Course,Lesson
# Create your views here.

@login_required
def index(request):
  
    courses = Course.objects.all()
    print(courses)
    context = {
        "courses" :courses,
    }
    return render(request,'index.html',context)
def lesson(request):
  
    lessons = Lesson.objects.all()
    context = {
        "lessons" :lessons,
    }
    return render(request,'lesson.html',context)
