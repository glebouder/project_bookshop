from django.db import models

class Langue(models.Model):
    id = models.AutoField(primary_key=True)
    langue = models.CharField(max_length=8)

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    theme = models.TextField()

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genre = models.TextField()

class Distributeur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.TextField()
    mail = models.TextField()
    tel = models.TextField()
    fax = models.TextField()
    adresse = models.ForeignKey('utilisateurs.Adresse')

class Editeur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.TextField()
    mail = models.TextField()
    distributeur = models.ForeignKey('Distributeur')
    adresse = models.ForeignKey('utilisateurs.Adresse')

class Auteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.TextField()
    prenom = models.TextField()
    nom_auteur = models.TextField()
    mail = models.TextField()

class Livre(models.Model):
    isbn = models.AutoField(primary_key=True)
    titre = models.TextField()
    prix = models.IntegerField()
    annee = models.IntegerField()
    quantite = models.IntegerField()
    langue = models.ForeignKey('Langue')
    editeur = models.ForeignKey('Editeur')

class Est_Genre(models.Model):
    id = models.AutoField(primary_key=True)
    id_genre = models.ForeignKey('Genre')
    id_livre = models.ForeignKey('Livre')

class Est_Theme(models.Model):
    id = models.AutoField(primary_key=True)
    id_theme = models.ForeignKey('Theme')
    id_livre = models.ForeignKey('Livre')

class A_Ecrit(models.Model):
    id = models.AutoField(primary_key=True)
    id_livre = models.ForeignKey('Livre')
    id_auteur = models.ForeignKey('Auteur')

