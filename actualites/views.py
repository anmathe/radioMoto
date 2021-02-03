
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .formulaire import ContactForm
from .models import Articles, Categories, sous_Categories, LesEditions, Emissions, AproposdeNous_NotreEquipe, AproposdeNous_laRadio, AproposdeNous_ProjetdAvenir


def index(request):
    article = Articles.objects.all()
    derniers = Articles.objects.order_by('date')[:4]
    data = {
        'article': article,
        'derniers' : derniers
        }
        # methode qui nous permet d afficher les articles
    return render(request,'actualites/index.html', data)
     


def actualités(request):
    article_actualites = Articles.objects.filter( Categories = 'actualites')
    return render(request,'actualites/actualités.html', {'article': article_actualites})
    

def noseditions(request):
    article_editions = LesEditions.objects.filter( Categories = 'nos Editions')
    return render(request,'actualites/noseditions.html', {'LesEditions': article_editions})
    

def emissions(request):
    article_Emissions = Emissions.objects.filter( Categories = 'emissions')
    return render(request,'actualites/emissions.html', {'LesEmissions':article_Emissions})
    

def apropos_de_nous(request):
    article_AboutUs = AproposdeNous_laRadio.objects.filter( Categories = 'la Radio')
    return render(request,'actualites/apropos_de_nous.html', {'a propos de nous':article_AboutUs })
    

def Notre_Equipe(request):
    article_team = AproposdeNous_NotreEquipe.objects.filter( Categories = 'notre Equipe')
    return render(request,'actualites/Notre_Equipe.html', {'Notre Equipe':article_team})


def Projet_d_Avenir(request):
    article_projects = AproposdeNous_ProjetdAvenir.objects.filter( Categories = 'notre Equipe')
    return render(request, 'actualites/Projet_d_Avenir.html', {'Notre Projects': article_projects})

def Nous_Contacter(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            Noms = form.cleaned_data['Noms']
            objet_Message = form.cleaned_data ['objet_Message']
            Mail= form.cleaned_data['Mail']
            message = form.cleaned_data['message']
            
            
            envoi = True
    else: 
        form = ContactForm() # Nous créons un formulaire vide

    return render(request, 'actualites/Nous_Contacter.html', {'form': form})


def Réligieuse(request):
    template = loader.get_template('actualites/Réligieuse.html')
    return HttpResponse(template.render(request=request))

def santé(request):
    template = loader.get_template('actualites/santé.html')
    return HttpResponse(template.render(request=request))

def Politique(request):
    template = loader.get_template('actualites/Politique.html')
    return HttpResponse(template.render(request=request))

def Economique(request):
    template = loader.get_template('actualites/Economique.html')
    return HttpResponse(template.render(request=request))

def Autres_Actualites(request):
    template = loader.get_template('actualites/Autres_Actualites.html')
    return HttpResponse(template.render(request=request))

def Emission_Réligieuse(request):
    template = loader.get_template('actualites/Emission_Réligieuse.html')
    return HttpResponse(template.render(request=request))

def Autres_Emissions(request):
    template = loader.get_template('actualites/Autres_Emissions.html')
    return HttpResponse(template.render(request=request))

def Française(request):
    template = loader.get_template('actualites/Française.html')
    return HttpResponse(template.render(request=request))

def Kinande(request):
    template = loader.get_template('actualites/Kinande.html')
    return HttpResponse(template.render(request=request))

def Swahili(request):
    template = loader.get_template('actualites/Swahili.html')
    return HttpResponse(template.render(request=request))

# Create your views here.template = loader.get_template('actualites/index.html')
