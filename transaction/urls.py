from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create-wallet/', views.addWallet, name='postwallet'),
    path('addtransaction/', views.addtransaction, name='addtransaction'),
    path('wallet-setting/', views.walletSetting, name='wallet-setting'),
    path('api/wallet/', views.getWallet, name='getwallet'),
    path('api/transaction/bargraph/',views.bargraph, name='bargraph'),
    path('api/wallet/changeWallet/', views.changeWalletSetting, name='changeWallet'),
    path('deleteWallet/', views.deleteWallet, name='deleteWallet')
]