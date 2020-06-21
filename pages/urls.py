from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('about/', views.aboutview, name='about')
]