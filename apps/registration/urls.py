from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from apps.registration.views import SigUpView, ProfileView

urlpatterns = [
    path('sign_up', SigUpView.as_view(), name='sign_up'),
    #path('sign_in', SignInView, name='sign_in'),
    #path('sign_out', SignOutView, name='sign_out'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('sign_in', auth_views.LoginView.as_view(template_name='registration/sign_in.html'), name='sign_in'),
    path('sign_out', auth_views.LogoutView.as_view(template_name='home/home.html'), name='sign_out'),
]
