from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('forgot-password/', views.forgot_password, name = 'forgot_password'),
    path('change-password/', views.change_password, name = 'change_password'),
    path('profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]