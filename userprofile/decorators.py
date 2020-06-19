
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

#   wrapper function middleware to prevent admin from entering the user routes
def is_admin(view_function) : 
    def wrapper_function(request, *args, **kwargs) : 
        if request.user.is_staff or request.user.is_superuser : 
            logout(request)
            messages.error(request, 'You were loggedin as an admin. You have been logged out and now login with your user credentials.')
            return redirect('/account/login/')
        return view_function(request, *args, **kwargs)

    return wrapper_function

