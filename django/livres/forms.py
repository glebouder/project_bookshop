from django.forms import ModelForm,ChoiceField,Form
from django import forms
from livres.models import *

class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'

class AuteurForm(ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'

class EditeurForm(ModelForm):
    class Meta:
        model = Editeur
        fields = '__all__'

class LangueForm(ModelForm):
    class Meta:
        model = Langue
        fields = '__all__'
    def is_valide():
        return(True)

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'

class SearchForm(Form):
    auteur = forms.CharField(label='auteur',max_length=100)
    editeur = forms.CharField(label='editeur',max_length=100)
    langue = forms.CharField(label='langue',max_length=100)
    genre = forms.CharField(label='genre',max_length=100)
    theme = forms.CharField(label='theme',max_length=100)
    titre = forms.CharField(label='titre',max_length=100)
