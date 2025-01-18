from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'signup.html', {})

def login(request):
    return render(request, 'login.html', {})

def forgot_password(request):
    return render(request, 'forgot_password.html', {})

def change_password(request):
    return render(request, 'change_password.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})