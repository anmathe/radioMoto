from django import forms
from django.forms import ModelForm
from .models import AproposdeNous_NousContacter

class ContactForm(ModelForm):
    
    class Meta:
        model = AproposdeNous_NousContacter
        fields = ('Noms_contact', 'objet_Message', 'mail', 'message' )

#class CommentairesForms(forms.Form):
#    message = forms.CharField(widget=forms.Textarea)
#    noms = Noms = forms.CharField(max_length=100)