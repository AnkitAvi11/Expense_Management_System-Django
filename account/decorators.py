
from django.shortcuts import redirect

#   decorator to check if the user is authenticated
def is_authenticated(view_function) : 
    def wrapper(request, *args, **kwargs) : 
        if request.user.is_authenticated : 
            return redirect('/')
        else : 
            return view_function(request, *args, **kwargs)

    return wrapper