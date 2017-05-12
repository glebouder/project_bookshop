from django.shortcuts import render
from django.views.generic. import FormView

from django.contrib.auth.forms import UserCreationForm


def registrationView(request):
    form_class = UserCreationForm

