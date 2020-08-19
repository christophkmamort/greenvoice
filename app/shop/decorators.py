from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:index')
        else:
            return view_func(self, request, *args, **kwargs)

    return wrapper_func
