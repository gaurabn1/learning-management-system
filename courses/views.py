from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Course
# Create your views here.

@login_required
def index(request):
    courses = Course.objects.all()
    print(courses)
    context = {
        "courses" :courses,
        'categories' : response
    }
    return render(request,'index.html',context)
