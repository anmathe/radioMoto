from django.db import models
from django.shortcuts import render
from django import forms

class Articles (models.Model):
    titre = models.CharField(max_length=500)
    imageArticle = models.ImageField(blank = True, null = True, upload_to="Galeries_RMO/") 
    slug = models.SlugField(max_length=100)
    corps_du_texte = models.TextField(null=True)

    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
  
    echoArticle = models.FileField(blank = True, null = True, upload_to='uploads/%Y/%m/%d/')
    auteur = models.CharField(max_length=42)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories")
    sous_Categories= models.ForeignKey('sous_Categories',on_delete = models.CASCADE, verbose_name="les sous categories")
    nombre_des_commentaires = models.IntegerField()
    nombre_des_vues = models.IntegerField()
    article_A_la_une =  models.BooleanField(verbose_name= ('A la Une'), default=False)

    class Meta:
        ordering = ['titre', '-date']

    def __str__(self):
        return self.titre


class Categories (models.Model):
    nomCat = models.CharField(max_length = 50)
    id_sous_categories = models.ForeignKey('sous_Categories',on_delete = models.CASCADE, verbose_name="les sous categories")

    def __str__(self):
        return self.nomCat
    

class sous_Categories (models.Model):
    nom_sousCat = models.CharField(max_length = 50)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)
    

    def __str__(self):
        return self.nom_sousCat


class AproposdeNous_laRadio ( models.Model):
    titreduMessage = models.CharField(max_length = 200, null= True)
    message_aux_auditeurs = models.TextField()
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)

    def __str__(self):
        return self.titreduMessage

    
class AproposdeNous_NotreEquipe(models.Model):
    nomdelEquipe = models.CharField(max_length =100, null = True )
    texteEquipe = models.TextField(null=True)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)

    def __str__(self):
        return self.nomdelEquipe


class AproposdeNous_ProjetdAvenir(models.Model):
    titreduProjet = models.CharField(max_length=200)
    objectifsProjet = models.TextField(null=True)
    contexteduProjet = models.TextField(null=False)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)

    def __str__(self):
        return self.titreduProjet 

class AproposdeNous_NousContacter(models.Model):
    Noms_contact = models.CharField(max_length = 200)
    objet_Message = models.CharField(max_length = 500)
    mail = models.EmailField(max_length = 200)
    message = models.TextField(null = False)
    
    def __str__(self):
        return self.Noms_contact


class Emissions(models.Model):
    titreEmission = models.CharField(max_length=200)
    EchoEmission = models.FileField(blank = True, null = True, upload_to='Emissions/%Y/%m/%d/')
    texteEmission = models.TextField(null=True)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)

    def __str__(self):
        return self.titreEmission 


class LesEditions (models.Model):
    deskEditions =  models.CharField(max_length=100)
    dateEditions = models.DateTimeField(auto_now_add=True, verbose_name = "date de l'Edition")
    enregistrementJournal = models.FileField(blank = True, null = True, upload_to='jounalsLangues/%Y/%m/%d/')
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories", null = True)

    def __str__(self):
        return self.deskEditions 