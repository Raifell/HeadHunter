from django import forms
from main.models import Resume, Vacancy
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'is_staff', 'password1', 'password2')
        labels = {
            'is_staff': 'Are you employer?'
        }


class CreateResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('title', 'name', 'surname', 'patronymic', 'birthdate',
                  'email', 'skills', 'experience', 'education')
        widgets = {
            'birthdate': forms.TextInput(attrs={'type': 'date'})
        }


class CreateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name', 'company', 'salary', 'skill', 'duty', 'address')
        labels = {
            'name': 'Title',
        }
