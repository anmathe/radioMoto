from django.db import models
from django.shortcuts import render

class Articles (models.Model):
    titre = models.CharField(max_length=500)
    imageArticle = models.ImageField(blank = True, null = True, upload_to="Galeries_RMO/") 
    slug = models.SlugField(max_length=100)
    corps_du_texte = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    echoArticle = models.FileField(blank = True, null = True, upload_to='uploads/%Y/%m/%d/')
    auteur = models.CharField(max_length=42)
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="les categories")
    nombre_des_commentaires = models.IntegerField()
    nombre_des_vues = models.IntegerField()

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
    

    def __str__(self):
        return self.nom_sousCat
    