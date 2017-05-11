from django.db import models
from django.utils import timezone

class Commandes(models.Model):
    id = models.AutoField(primary_key=True)
    date_emmission = models.DateTimeField(default=timezone.now)
    type = models.IntegerField()
    quantite = models.IntegerField()
    expediee = models.BooleanField(default=False)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    adresse = models.ForeignKey('utilisateurs.Adresse')
    commanditaire = models.ForeignKey('utilisateurs.Utilisateur')
    produit = models.ForeignKey('livres.Livre')


