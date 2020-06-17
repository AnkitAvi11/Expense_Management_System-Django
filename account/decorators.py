
from django.shortcuts import redirect

def is_authenticated(view_function) : 
    def wrapper(request, *args, **kwargs) : 
        if request.user.is_authenticated : 
            return redirect('/')
        else : 
            return view_function(request, *args, **kwargs)

    return wrapper