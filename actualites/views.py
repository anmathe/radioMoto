
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
#from .models import Categories, Articles


def index(request):
    #articles = Articles.objects.all() 
    template = loader.get_template('actualites/index.html')
    return HttpResponse(template.render(request=request))

def actualités(request):
    template = loader.get_template('actualites/actualités.html')
    return HttpResponse(template.render(request=request))
    # message = "salut tout le monde ici les actualites"
    #return HttpResponse(message)

def noseditions(request):
    template = loader.get_template('actualites/noseditions.html')
    return HttpResponse(template.render(request=request))
    #message = "salut tout le monde ici Editions"
    #return HttpResponse(message)

def emissions(request):
    template = loader.get_template('actualites/emissions.html')
    return HttpResponse(template.render(request=request))

def apropos_de_nous(request):
    template = loader.get_template('actualites/apropos_de_nous.html')
    return HttpResponse(template.render(request=request))

def La_Radio(request):
    template = loader.get_template('actualites/La_Radio.html')
    return HttpResponse(template.render(request=request))
    #message = "salut tout le monde c'est à propos des nous"
    #return HttpResponse(message)

def Notre_Equipe(request):
    template = loader.get_template('actualites/Notre_Equipe.html')
    return HttpResponse(template.render(request=request))

def Projet_d_Avenir(request):
    template = loader.get_template('actualites/Projet_d_Avenir.html')
    return HttpResponse(template.render(request=request))

def Nous_Contacter(request):
    template = loader.get_template('actualites/Nous_Contacter.html')
    return HttpResponse(template.render(request=request))

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

def search (request):
    obj = str(request.GET)
    query = request.GET['query']
    return HttpResponse(query)
"""
def lire_Article (request, id_Articles):

    article = Articles.objects.get(id=id)
    return render(request, 'actualites/lire.html', {{ article}})
"""
# Create your views here.
