from django.shortcuts import render, redirect
from account.forms import CustomUserForm, UserLoginForm
from account.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    form  = UserLoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
            
    return render(request, 'login.html', {"form": form})


def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()       
            return redirect('login')
        
    return render(request, 'register.html', {"form": form})
