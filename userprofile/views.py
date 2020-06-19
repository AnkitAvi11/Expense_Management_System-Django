from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from account.validators import isEmail, isUserName
from .decorators import is_admin

#   user dashboard
@login_required(login_url='/account/login/')
@is_admin
def get_profile(request) :
    user = User.objects.get(id=request.user.id)
    context = {
        "profile" : user
    }
    return render(request, 'account/dashboard.html', context)

#   edit user profile method
@login_required(login_url='/account/login/')
@is_admin
def edit_user_profile(request) : 
    if request.method == 'POST' : 
        userid = request.user.id
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        if isEmail(email) and isUserName(username) : 
            user = User.objects.get(id=userid)

            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.username = username
            user.userprofile.user_bio = bio
            user.userprofile.save()
            user.save()

            messages.success(request, 'Changes made successfully!')
            return redirect('/profile/edit-profile/')
        else : 
            messages.error(request, "Enter a valid username and email")
            return redirect('/profile/edit-profile/')

    else : 
        return render(request, 'account/editprofile.html')


@login_required
@is_admin
def user_setting(request) : 
    return render(request, 'account/setting.html')
