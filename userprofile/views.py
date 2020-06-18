from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from account.validators import isEmail, isUserName

#   home
@login_required(login_url='/account/login/')
def get_profile(request) :
    user = User.objects.get(id=request.user.id)
    context = {
        "profile" : user
    }
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='/account/login/')
def edit_user_profile(request) : 
    if request.method == 'POST' : 
        userid = request.POST.get('user_id')
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')

        if isEmail(email) and isUserName(username) : 
            user = User.objects.get(id=userid)

            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.username = username
            user.save()

            messages.success(request, 'Changes made successfully!')
            return redirect('/profile/edit-profile/')
        else : 
            messages.error(request, "Enter a valid username and email")
            return redirect('/profile/edit-profile/')

    else : 
        return render(request, 'account/editprofile.html')
