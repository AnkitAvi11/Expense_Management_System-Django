from django.urls import path, re_path

from . import views

urlpatterns = [
    path('dashboard/', views.get_profile, name='profile'),
    path('edit-profile/', views.edit_user_profile, name='editprofile'),
]
