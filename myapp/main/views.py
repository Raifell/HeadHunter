from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vacancy, Resume
from .forms import CreateUserForm, CreateResumeForm, CreateVacancyForm

# ------------------------------------- Main Page ------------------------------------------


class MainPageView(ListView):
    model = Resume
    template_name = 'main/index_main.html'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                self.extra_context['title'] = 'Resume list'
                self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'} #
                self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
            else:
                self.extra_context['title'] = 'Vacancy list'
                self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
                self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff:
            return {'resume': Resume.objects.all()}
        else:
            return {'vacancy': Vacancy.objects.all()}


# ------------------------------ Block Vacancy CRUD --------------------------------


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'main/index_vacancy_list.html'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Vacancy list'
            self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
            self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Vacancy.objects.filter(user__username=self.request.user.username)


class VacancyPageView(DetailView):
    model = Vacancy
    template_name = 'main/index_vacancy_detail.html'
    slug_url_kwarg = 'vacancy_slug'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                self.extra_context['title'] = 'Vacancy'
                self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
                self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
            else:
                self.extra_context['title'] = 'Vacancy'
                self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
                self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


class CreateVacancyPage(CreateView):
    template_name = 'main/index_vacancy_create.html'
    form_class = CreateVacancyForm
    success_url = reverse_lazy('main_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Create Vacancy'
            self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
            self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.cleaned_data['user'] = User.objects.get(username=self.request.user.username)
        Vacancy.objects.create(**form.cleaned_data)
        return redirect('main_page')


class UpdateVacancyView(UpdateView):
    model = Vacancy
    template_name = 'main/index_vacancy_create.html'
    slug_url_kwarg = 'vacancy_slug'
    form_class = CreateVacancyForm
    success_url = reverse_lazy('list_vacancy_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Update Vacancy'
            self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
            self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


class DeleteVacancyView(DeleteView):
    model = Vacancy
    template_name = 'main/index_vacancy_delete.html'
    slug_url_kwarg = 'vacancy_slug'
    context_object_name = 'data'
    success_url = reverse_lazy('list_vacancy_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Delete Vacancy'
            self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
            self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


# ------------------------------ Block Resume CRUD --------------------------------


class ResumeListView(ListView):
    model = Resume
    template_name = 'main/index_resume_list.html'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'My Resume(s)'
            self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Resume.objects.filter(user__username=self.request.user.username)


class ResumePageView(DetailView):
    model = Resume
    template_name = 'main/index_resume_detail.html'
    slug_url_kwarg = 'resume_slug'
    context_object_name = 'data'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                self.extra_context['title'] = 'Resume'
                self.extra_context['create'] = {'name': 'Create Vacancy', 'path': 'create_vacancy_page'}  #
                self.extra_context['list'] = {'name': 'My Vacancy(s)', 'path': 'list_vacancy_page'}
            else:
                self.extra_context['title'] = 'Resume'
                self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
                self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
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
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.cleaned_data['user'] = User.objects.get(username=self.request.user.username)
        Resume.objects.create(**form.cleaned_data)
        return redirect('main_page')


class UpdateResumeView(UpdateView):
    model = Resume
    template_name = 'main/index_resume_create.html'
    slug_url_kwarg = 'resume_slug'
    form_class = CreateResumeForm
    success_url = reverse_lazy('list_resume_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Update Resume'
            self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


class DeleteResumeView(DeleteView):
    model = Resume
    template_name = 'main/index_resume_delete.html'
    slug_url_kwarg = 'resume_slug'
    context_object_name = 'data'
    success_url = reverse_lazy('list_resume_page')
    extra_context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.extra_context['title'] = 'Delete Resume'
            self.extra_context['create'] = {'name': 'Create Resume', 'path': 'create_resume_page'}
            self.extra_context['list'] = {'name': 'My Resume(s)', 'path': 'list_resume_page'}
        else:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)

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
