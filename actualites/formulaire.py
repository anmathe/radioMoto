from django import forms
"""from models import Categories, sous_Categories

class Categories_formulaire(forms.ModelsForm):
    nomCat = forms.CharField(max_length = 50)
    class Meta :
        model = Categories
class sous"""

class ContactForm(forms.Form):

    Noms = forms.CharField(max_length=100)
    objet_Message = forms.CharField(max_length=300)
    Mail = forms.EmailField(label="Votre adresse mail")
    message = forms.CharField(widget=forms.Textarea)

class CommentairesForms(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    noms = Noms = forms.CharField(max_length=100)