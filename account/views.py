from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from . import validators
from .decorators import is_authenticated

#   function to deal with register functionality
@is_authenticated
def register(request) : 
    if request.method == 'POST' : 
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        profile = request.FILES.get('profile','default.png')

        #   validating username and email address
        if validators.isEmail(email) and validators.isUserName(username) : 

            #   checking if the user with that email or username already exist
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists() : 
                messages.error(request, 'User with that email or username aleady exist')
                return redirect('/account/register/')

            else : 
                
                #   when the user doesn't exist we create a new one
                user = User.objects.create_user(first_name=fname, last_name=lname, username=username,email=email, password=password1)
                user.save()
                user_profile = UserProfile(user = user,user_name=username, profile_pic = profile)
                user_profile.save()
                messages.success(request, 'User created succesfully')
                return redirect('/account/register/')

        else : 
            messages.error(request, 'Username or Email not valid')
            return redirect('/account/register/')            

    else : 
        return render(request, 'account/register.html',)

def login(request) : 
    return HttpResponse('Login page')

def logout(request) : 
    return HttpResponse('Logout')
