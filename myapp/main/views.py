from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vacancy, Resume
from .forms import CreateUserForm, CreateResumeForm


class MainPageView(ListView):
    model = Resume
    template_name = 'main/index_main.html'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                self.extra_context['title'] = 'Resume list'
                self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_resume_page'} #
                self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': ''}
            else:
                self.extra_context['title'] = 'Vacancy list'
                self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
                self.extra_context['list'] = {'name': 'My Resume(s)', 'path': ''}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff:
            return {'resume': Resume.objects.all()}
        else:
            return {'vacancy': Vacancy.objects.all()}


class VacancyPageView(DetailView):
    model = Vacancy
    template_name = 'main/index_vacancy_detail.html'
    slug_url_kwarg = 'vacancy_slug'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Vacancy'
            self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': ''}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


# ------------------------------ Resume CRUD --------------------------------

class ResumePageView(DetailView):
    model = Resume
    template_name = 'main/index_resume_detail.html'
    slug_url_kwarg = 'resume_slug'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Resume'
            self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_resume_page'} #
            self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': ''}
        else:
            return redirect('login_page')
        print()
        print(type(Resume.objects.get(slug=kwargs[self.slug_url_kwarg]).user))
        print()
        return super().get(request, *args, **kwargs)


class CreateResumePage(CreateView):
    template_name = 'main/index_resume_create.html'
    form_class = CreateResumeForm
    success_url = reverse_lazy('main_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Create Resume'
            self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': ''}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.cleaned_data['user'] = User.objects.get(username=self.request.user.username)
        Resume.objects.create(**form.cleaned_data)
        return redirect('main_page')

# -------------------------------- Block Login/Logout/Register User --------------------------------


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


def logout_view(request):
    logout(request)
    return redirect('main_page')
