from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
from apps.registration.forms import RegistrationForm
from django.urls import reverse_lazy

# Create your views here.

""" class SigUpView(TemplateView):
    template_name = 'registration/sign_up.html' """

""" class SigInView(TemplateView):
    template_name = 'registration/sign_in.html' """

class SigUpView(CreateView):
    model = User
    template_name = 'registration/sign_up.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('task')

class ProfileView(TemplateView):
    template_name = 'profile/profile.html'

""" def SignInView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('task')

    return render(request, 'registration/sign_in.html',{})

def SignOutView(request):
    logout(request)
    return redirect('home') """