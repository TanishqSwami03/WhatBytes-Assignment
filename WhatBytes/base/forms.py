from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    

class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)