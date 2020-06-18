from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name='logout'),
]