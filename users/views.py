from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('yummy_receitas:inicial'))

def login(request):
    """Log an existing user in"""
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login_auth(request, user)
                return HttpResponseRedirect(reverse('yummy_receitas:inicial'))
    
    return render(request, 'login.html')


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        email = request.POST['email']
        password = request.POST['senha']
        user = User.objects.create_user(email, password)
        user.set_password(password)
        user.save()
        authenticated_user = authenticate(email=email, password=password)
        login_auth(request, authenticated_user)
        return HttpResponseRedirect(reverse('yummy_receitas:inicial'))