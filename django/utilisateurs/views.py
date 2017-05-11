from django.shortcuts import render
from django.utils import timezone #ne sert pas pour l'instant
from .models import Utilisateur

def accueil(request):
    users = Utilisateur.objects.filter(nom__contains='').order_by('nom')
    return render(request, 'utilisateurs/accueil.html',{'users':users})

def login(request):
    return render(request, 'utilisateurs/login.html', {})

def register(request):
    return render(request, 'utilisateurs/register.html', {})
