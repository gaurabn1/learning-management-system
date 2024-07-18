from django.shortcuts import render, redirect
from account.forms import CustomUserForm, UserLoginForm
from account.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
# Create your views here.



def login(request):
    form  = UserLoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You are logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid user credentials.")
            return redirect('login')
            
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
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field} : {error}")
                    return redirect('register')
           
    return render(request, 'register.html', {"form": form})


def logout(request):
    user = request.user
    if user:
        auth_logout(request)
        return redirect('index')
