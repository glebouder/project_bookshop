from django.shortcuts import render,redirect
from .forms import *
from .models import *

def search(request):
    if request.method == "POST":
        print("popopopopopo")
        form = SearchForm(request.POST)
        print(form)
        print(form.cleaned_data)
        datas = form.cleaned_data
        auteurs = Auteur.objects.filter(nom_auteur__icontains=datas['auteur']).values()
        print(auteurs)
        #reponse = Livre.objects.filter(auteur__icontains=datas['auteur'])
            #faire la requete (.filter)
            #return answer(request,1)

    else:
        form=SearchForm()
    return render(request, 'livre/search.html', {'toto':form})


def answer(request,page):
    return render(request, 'livre/answer.html', {'res':['Livre']})


def add_sth(request, classe):
    dict_form = {
            'livre':LivreForm,
            'auteur':AuteurForm,
            'editeur':EditeurForm,
            'langue':LangueForm,
            'genre':GenreForm,
            'theme':ThemeForm,
    }
    dict_obj = {
            'livre':Livre,
            'auteur':Auteur,
            'editeur':Editeur,
            'langue':Langue,
            'genre':Genre,
            'theme':Theme,
    }
    type_form = dict_form[classe]
    type_obj = dict_obj[classe]
    if request.method == "POST":
        user_form = type_form(request.POST)
        print(user_form)
        if user_form.is_valide:
            print(user_form.cleaned_data)
            obj = type_obj(**user_form.cleaned_data)
            try:
                obj.save()
            except:
                return render(request, 'livre/add.html', {'already_exists':True})
            return redirect("add")
        else:
            print("not valide")
            type_form = user_form
    return render(request, 'livre/add_sth.html', {'item':type_form})


def add(request):
    return render(request, 'livre/add.html', {})


