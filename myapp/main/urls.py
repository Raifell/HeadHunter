from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('register/', views.RegisterPageView.as_view(), name='register_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('vacancy/<slug:vacancy_slug>/', views.VacancyPageView.as_view(), name='vacancy_page'),
    path('create-vacancy/', views.CreateVacancyPage.as_view(), name='create_vacancy_page'),
    path('list-vacancy/', views.VacancyListView.as_view(), name='list_vacancy_page'),
    path('update-vacancy/<slug:vacancy_slug>/', views.UpdateVacancyView.as_view(), name='update_vacancy_page'),
    path('delete-vacancy/<slug:vacancy_slug>/', views.DeleteVacancyView.as_view(), name='delete_vacancy_page'),
    path('resume/<slug:resume_slug>/', views.ResumePageView.as_view(), name='resume_page'),
    path('create-resume/', views.CreateResumePage.as_view(), name='create_resume_page'),
    path('list-resume/', views.ResumeListView.as_view(), name='list_resume_page'),
    path('update-resume/<slug:resume_slug>/', views.UpdateResumeView.as_view(), name='update_resume_page'),
    path('delete-resume/<slug:resume_slug>/', views.DeleteResumeView.as_view(), name='delete_resume_page'),
]
