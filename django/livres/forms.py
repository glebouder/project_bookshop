from django.forms import ModelForm,ChoiceField,Form
from django import forms
from livres.models import *

class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'
    def is_valide():
        return(True)

class AuteurForm(ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'
        def __init(self, *args, **kwargs):
            super(AuteurForm, self).__init(*args, **kwargs)
            self.fields['mail'].requided = False
    def is_valide():
        return(True)

class EditeurForm(ModelForm):
    class Meta:
        model = Editeur
        fields = '__all__'
    def is_valide():
        return(True)

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
    def is_valide():
        return(True)

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
    def is_valide():
        return(True)

class SearchForm(Form):
    auteur = forms.CharField(label='auteur',max_length=100,required=False)
    editeur = forms.CharField(label='editeur',max_length=100,required=False)
    langue = forms.CharField(label='langue',max_length=100,required=False)
    genre = forms.CharField(label='genre',max_length=100,required=False)
    theme = forms.CharField(label='theme',max_length=100,required=False)
    titre = forms.CharField(label='titre',max_length=100,required=False)
    def is_valide():
        return(True)
