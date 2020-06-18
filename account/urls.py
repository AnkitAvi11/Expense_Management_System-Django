from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    #   password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #   email sent view
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #   email reset confirmation with token
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #   password reset done
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]