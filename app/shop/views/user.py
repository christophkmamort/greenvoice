from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from shop.decorators import unauthenticated_user
from users.forms import CustomUserCreationForm


class LoginView(TemplateView):
    template_name = 'shop/login.html'

    @unauthenticated_user
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


    # @unauthenticated_user
    def post(self, request):
        email = request.POST.get('loginEmail')
        password =request.POST.get('loginPassword')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if request.POST.get('next'):
                next = request.POST.get('next', '/')
            else:
                next = '/'
            return HttpResponseRedirect(next)
        else:
            messages.info(request, 'E-Mail oder Passwort ist falsch.')

        context = {'submittedLoginEmail': email}
        return render(request, self.template_name, context)


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login?logout=success')


class RegisterView(TemplateView):
    template_name = 'shop/register.html'

    @unauthenticated_user
    def get(self, request):
        form = CustomUserCreationForm()

        context = {'form':form}
        return render(request, self.template_name, context)

    @unauthenticated_user
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account für '+ email +' erfolgreich erstellt.')

            return redirect('shop:login')

        context = {'form':form,}
        return render(request, 'accounts/register.html', context)
