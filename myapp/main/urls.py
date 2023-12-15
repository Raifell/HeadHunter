from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('register/', views.RegisterPageView.as_view(), name='register_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('vacancy/<slug:vacancy_slug>/', views.VacancyPageView.as_view(), name='vacancy_page'),
    path('resume/<slug:resume_slug>/', views.ResumePageView.as_view(), name='resume_page'),
    path('create-resume/', views.CreateResumePage.as_view(), name='create_resume_page'),
]
