from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect

#   django imports
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

#   account app files
from .models import UserProfile
from . import validators
from .decorators import is_authenticated

#   function to deal with register functionality
@is_authenticated
def registerUser(request) : 
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

#   function handling the login authentication
@is_authenticated
def loginUser(request) : 
    redirected_url = request.GET.get('next', '/')
    if request.method == 'POST' : 
        username_email = request.POST.get('username')
        password = request.POST.get('password1')
        if validators.isEmail(username_email) : 
            if not User.objects.filter(email=username_email).exists() : 
                messages.error(request, "User with that credentials doesn't exist")
                return redirect('/account/login/')
            else : 
                username = User.objects.get(email=username_email).username
        else :
            username = username_email

        #   authenticating user
        user = authenticate(username=username, password=password)
        if user is not None :   
            login(request, user)
            return redirect(redirected_url)
        else :      #   authentication failed
            messages.error(request, 'Incorrect username or password')
            return redirect('/account/login/?next='+redirected_url)
    else : 
        return render(request, 'account/login.html', {"next":redirected_url})


#   logout method
def logoutUser(request) : 
    if request.method == 'POST' : 
        logout(request)
        return redirect('/')
    else : 
        raise Http404()
