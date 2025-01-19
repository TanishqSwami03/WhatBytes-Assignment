from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name = 'login-user'),
    path('signup/', views.signup, name = 'signup'),
    path('logout-user/', views.logout_user, name = 'logout-user'),
    path('forgot-password/', views.forgot_password, name = 'forgot-password'),
    path('reset_password/<int:user_id>/<str:token>/', views.reset_password, name='reset_password'),
    path('change-password/', views.change_password, name = 'change-password'),
    path('profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]