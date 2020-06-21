from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from userprofile.decorators import is_admin

def indexView(request) : 
    if request.user.is_authenticated : 
        return redirect('/profile/dashboard/')
    else : 
        return render(request, 'pages/home.html')

def aboutview(request) : 
    return HttpResponse('about page')

#   view function for the 
@login_required(login_url='/account/login/')
@is_admin
def alltransactions(request) : 
    pass