from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vacancy, Resume
from .forms import CreateUserForm


class MainPageView(ListView):
    model = Resume
    template_name = 'main/index_main.html'
    context_object_name = 'data'
    extra_context = {
        'title': 'Main',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                self.extra_context['create'] = {'name': 'Create Vacancy', 'path': ''}
                self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': ''}
                # self.extra_context['vacancy'] = Vacancy.objects.all()
            else:
                self.extra_context['create'] = {'name': 'Create Resume', 'path': ''}
                self.extra_context['list'] = {'name': 'My Resume(s)', 'path': ''}
                # self.extra_context['resume'] = Resume.objects.all()
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Vacancy.objects.all()
        else:
            return Resume.objects.all()


class LoginPageView(LoginView):
    template_name = 'main/index_login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main_page')
    extra_context = {
        'title': 'Login'
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)


class RegisterPageView(CreateView):
    template_name = 'main/index_register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login_page')
    extra_context = {
        'title': 'Register',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)
