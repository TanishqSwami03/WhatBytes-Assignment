from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from .forms import *
from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created !")
            return redirect('login-user')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("user authenticated !!")
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)

    print("user logged out !")
    
    return redirect('login-user')

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = CustomUser.objects.get(email=email)
                
                token = default_token_generator.make_token(user)
                reset_url = request.build_absolute_uri(f"/reset_password/{user.pk}/{token}/")
                
                
                send_mail(
                    'Password Reset Instructions',
                    f'Click the link below to reset your password:\n{reset_url}',
                    'no-reply@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Password reset instructions have been sent to your email.')
                return redirect('login-user')
            except CustomUser.DoesNotExist:
                messages.error(request, 'No user found with that email address.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})

def reset_password(request, user_id, token):
    try:
        user = CustomUser.objects.get(pk=user_id)
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = SetPasswordForm(user=user, data=request.POST)
                if form.is_valid():
                    
                    user.set_password(form.cleaned_data['new_password1'])
                    user.last_updated = now()
                    user.save()

                    messages.success(request, 'Your password has been reset successfully.')
                    return redirect('login-user')
                else:
                    messages.error(request, 'Please correct the errors below.')
            else:
                form = SetPasswordForm(user=user)
            return render(request, 'reset_password.html', {'form': form})
        else:
            messages.error(request, 'The reset link is invalid or has expired.')
            return redirect('forgot_password')
    except CustomUser.DoesNotExist:
        messages.error(request, 'User does not exist.')
        return redirect('forgot_password')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            user.last_updated = now()
            user.save()
            messages.success(request, "Your password has been successfully changed.")
            return redirect('change-password')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            
            return redirect('change-password')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {})

@login_required
def dashboard(request):

    user = request.user

    if user.is_authenticated:
        print("user authenticated")
    

        return render(request, 'dashboard.html', {})

    else:
        return render(request, 'login.html', {})