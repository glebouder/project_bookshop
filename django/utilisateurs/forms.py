from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur (pseudo)', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Mot de passe (à nouveau)', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Les deux mots de passe diffèrent')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Le nom d\'utilisateur doit contenir seulement des caractères alphanumériques et des underscore (\'_\').')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Ce nom d\'utilisateur existe déjà.')
            

