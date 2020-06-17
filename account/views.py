from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def register(request) : 
    return render(request, 'account/register.html',)

def login(request) : 
    return HttpResponse('Login page')

def logout(request) : 
    return HttpResponse('Logout')
