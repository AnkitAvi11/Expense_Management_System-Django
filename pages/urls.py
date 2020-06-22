from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('about/', views.aboutview, name='about'),
    path('transaction/', views.transactions_page, name="transaction"),
    path('new-wallet/', views.newwallet, name='newwallet'),
]