from django.urls import path, re_path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('change-password/', views.changepassword, name='changepassword'),
    path('change-profile/', views.change_profile_pic, name="change-profile"),
    path('delete-account/', views.deleteuseraccount, name='delete-user'),

    #   setting up the urls for password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='resetpassword/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='resetpassword/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetpassword/change.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='resetpassword/complete.html'), name='password_reset_complete')
]

"""
NOW ALL I NEED IN THIS APPLICATION IS A WAY FOR THE USERS TO RESET PASSWORD
    1. PASSWORD_RESET
    2. PASSWORD_RESET_DONE
    3. RESET/<UIDB64>/<TOKEN> (PASSWORD_RESET_CONFIRM)
    4. RESET/DONE/  PASSWORD_RESET_COMPLETE
"""