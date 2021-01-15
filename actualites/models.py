from django.db import models
from django.shortcuts import render

#l'unique table dans notre base des donnees c'est l'article avec tous ces champs en parametre
class Articles (models.Model):
    titre = models.CharField(max_length=500)
    imageArticle = models.ImageField(upload_to="Galeries_RMO/") 
    slug = models.SlugField(max_length=100)
    corps_du_texte = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    echoArticle = models.FileField(upload_to='uploads/%Y/%m/%d/')
    auteur = models.CharField(max_length=42)
    Categories = models.ForeignKey('Categories',on_delete=models.CASCADE,verbose_name="les categories")
    

    def __str__(self):
        return self.titre


class Categories (models.Model):
    nomCat = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nomCat

class sous_Categories (models.Model):
    nom_sousCat = models.CharField(max_length = 50)
    id_categorie = models.ForeignKey('categories',on_delete = models.CASCADE, verbose_name="les sous categories")
    
    def __str__(self):
        return self.nom_sousCat

#class commentaires_visiteurs(models.model)