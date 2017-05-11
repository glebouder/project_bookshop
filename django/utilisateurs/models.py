from django.db import models
from django.utils import timezone

class Type_Voie(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=40)

class Adresse(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    nom = models.CharField(max_length=100)
    commune = models.CharField(max_length=101)
    cp = models.IntegerField()
    type_voie = models.ForeignKey('Type_Voie')

class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    mdp = models.CharField(max_length=64)
    pseudo = models.TextField()
    nom = models.TextField()
    prenom = models.TextField()
    mail = models.TextField()
    tel = models.TextField()
    adresse = models.ForeignKey('Adresse',default=1)

    def change_prenom(self,new_prenom):
        self.prenom = new_prenom

