from django.db import models
from django import forms
from utilisateurs.models import Type_Voie,Adresse,Utilisateur
from livres.models import Langue,Theme,Genre,Distributeur,Editeur,Auteur,Livre
from commandes.models import Commande

#class LoginForm(forms.ModelForm):
#    class Meta:
#        model = Utilisateur
#        fields = ['pseudo','mdp']
