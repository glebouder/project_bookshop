from django.shortcuts import render
from .forms import *

def search(request):
    return render(request, 'livres/search.html', {})

def answer(request,page):
    return render(request, 'livre/answer.html', {})

def add(request):
    print(request.method)
    if request.method=="POST":
        print(request.POST)
        print("lalallalalalllallallallla")
        print(request.POST['object'])
        return (3)
        # On doit faire truc.create
    elif request.method=="GET":
        return render(request, 'livre/add.html', {})
    else:
        raise("don't know what to do with "+request.method+" in add")

def add_sth(request, classe):
    dict = {
            'livre':LivreForm(),
            'auteur':AuteurForm(),
            'editeur':EditeurForm(),
            'langue':LangueForm(),
            'genre':GenreForm(),
            'theme':ThemeForm(),
    }
    form=print(dict[classe])
    return render(request, 'livre/add_sth.html', {'classe':dict[classe]})


# Create your views here.
