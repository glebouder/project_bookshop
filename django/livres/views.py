from django.shortcuts import render,redirect
from .forms import *

def search(request):
    return render(request, 'livres/search.html', {})


def answer(request,page):
    return render(request, 'livre/answer.html', {})


def add(request):
#    print(request.method)
#    # Si l'utilisateur a rempli le  formulaire,
#    # On check s'il est bien, et si oui on envoie l'utilisateur où il faut
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            return redirect('')
#
#    # Sinon, l'utilisateur veut le formulaire, on lui envoie
#    else:
#        print("toto")
    return render(request, 'livre/add.html', {})
#        form = ChoiceForm(widget=forms.Select)
#        print("iiiiiiiiiiiiiiiiiii")
#        print(form)
#        print(form.choices)
#    return render(request, 'livre/add.html', {'form':form})

#def add(request):
#    # Si on vient de cette page et qu'on a rempli le formulaire,
#    # Alors on redirige vers la bonne page avec add_sth
#    if request.method=="POST":
#        objet = request.POST.get('object')
#        request.method = "GET"
#        return (add_sth(request,objet))
#
#    # Si on arrive sur la page pour la première fois,
#    # Alors on fournit le formulaire
#    elif request.method=="GET":
#        return render(request, 'livre/add.html', {})
#
#    # Éventuellement on ne sait pas quoi faire
#    else:
#        raise("don't know what to do with "+request.method+" in add")

def add_sth(request, classe):
    print("add_sth")
    print(classe)
    print(request.method)
    dict_form = {
            'livre':LivreForm(),
            'auteur':AuteurForm(),
            'editeur':EditeurForm(),
            'langue':LangueForm,
            'genre':GenreForm(),
            'theme':ThemeForm(),
    }
    toto = Langue.objects
    type_form = dict_form[classe]
    if request.method == "POST":
        user_form = type_form(request.POST)
        print(request.POST['sigle'])
        print(user_form)
        if user_form.is_valide:
            print(user_form.cleaned_data)
            answers = request.POST
#            answers['sigle'] = answers['sigle'].lower()
#            if Langue.objects.get(sigle__=(answers['sigle'])):
#                print("already exists")
#            else:
#                print("newone")
            print("succeded")
            # on ajoute paar requete , en vérifiant qu'on n'a pas déjà la langue
            Langue.objects.create(user_form.cleaned_data)
            print("lalalallalalalla")
            return redirect("add")
        else:
            print("not valide")
            type_form = user_form
    return render(request, 'livre/add_sth.html', {'item':type_form , 'classe':classe})

