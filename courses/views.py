from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Course
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    
    if request.GET.get('search'):
        query = request.GET.get('search')
        courses = Course.objects.filter(title__icontains = query)
        if not courses:
            messages.error(request, "Course not Found.")
            return redirect('index')
    else:
        courses = Course.objects.all()

    context = {
        "courses" :courses,
    }
    return render(request,'index.html',context)


