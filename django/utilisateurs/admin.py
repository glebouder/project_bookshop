from django.contrib import admin
from .models import Utilisateur
from .models import Adresse
from .models import Type_Voie

admin.site.register(Utilisateur)
admin.site.register(Adresse)
admin.site.register(Type_Voie)
