from django.forms import ModelForm
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

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
