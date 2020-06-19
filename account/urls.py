from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('change-password/', views.changepassword, name='changepassword'),
    path('change-profile/', views.change_profile_pic, name="change-profile"),
    path('delete-account/', views.deleteuseraccount, name='delete-user'),
]