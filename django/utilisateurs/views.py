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
#    return redirect('accueil') (ne marche pas, on verra plus tard)

def my_account(request):
    return render(request, 'utilisateurs/my_account.html', {})

def new_account(request):
    return render(request, 'registration/new_account.html',{})


def register(request):
    if request.method == 'POST':
#        print(request.POST)
        form = RegistrationForm(request.POST)
        created = False
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/login/')
        form = RegistrationForm()
        variables = {'form': form}
        return render_to_response('registration/register.html',variables)
    return('toto')






#def register(request):
#    if request.method =='POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
#            user.save()
#            return render_to_response('QCM/index.html') # Redirect after POST
#        else:
#            form = UserCreationForm() # An unbound form
#
#            return render_to_response('register.html', {
#                'form': form,
#            },context_instance=RequestContext(request))
#

#    form = LoginForm(request.POST or None)
#    if form.is_valide():
#        pseudo = form.cleaned_data['pseudo']
#        mdp = form.cleaned_data['mdp']
#        if (Utilisateur.objects.get(pseudo=pseudo,mdp=mdp)):
#            true=True
#        else:
#            true=False
#





#def login(request):
#    username = request.POST['pseudo']
#    password = request.POST['mdp']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        return render(request, 'utilisateurs/my_account.html', {})
#    else:
#        return render(request, 'utilisateurs/login.html', {})

#def register(request):
#    return render(request, 'utilisateurs/register.html', {})

#    return render(request, 'utilisateur/my_account.html', locals())
