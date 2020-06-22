from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create-wallet/', views.addWallet, name='postwallet'),
    path('addtransaction/', views.addtransaction, name='addtransaction')
]