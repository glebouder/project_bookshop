from django.shortcuts import render,render_to_response
from django.utils import timezone #ne sert pas pour l'instant
from .models import Utilisateur
from utilisateurs.forms import *
from django.contrib.auth import logout
from django.template import RequestContext
from django.http import HttpResponseRedirect

def accueil(request):
    users = User.objects.all().order_by('id')
    print(len(users))
    return render(request, 'utilisateurs/accueil.html', {'users':users})

def logout(request):
    logout(request)

def my_account(request):
    return render(request, 'utilisateurs/my_account.html', {})

def new_account(request):
    return render(request, 'registration/new_account.html',{})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        created = False
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/login/')
        form = RegistrationForm()
        variables = {'form': form}
        return render_to_response('registration/register.html',variables)
    return('toto')

