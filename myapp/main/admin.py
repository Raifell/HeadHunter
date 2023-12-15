from django.contrib import admin
from .models import Resume, Vacancy


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'surname', 'patronymic', 'birthdate', 'email')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'salary', 'address')


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Vacancy, VacancyAdmin)
