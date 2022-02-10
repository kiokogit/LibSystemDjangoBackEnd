from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutFunc, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard')
];
