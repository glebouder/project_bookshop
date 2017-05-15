from django.shortcuts import render,redirect
from .forms import *
from .models import *

def search(request):
    if request.method == "POST":
        print("popopopopopo")
        form = SearchForm(request.POST)
        print(form)
        #if form.is_valide: #bordel...
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


