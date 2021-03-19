
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect 
from django.forms import ModelForm
from .formulaire import ContactForm
from django.core.mail import BadHeaderError, send_mail
from .models import AproposdeNous_NousContacter
from .models import Articles, Categories, sous_Categories, LesEditions, Emissions, AproposdeNous_NotreEquipe, AproposdeNous_laRadio, AproposdeNous_ProjetdAvenir


def index(request):
    article = Articles.objects.all()
    art = list(Articles.objects.values())
    articleSlides= Articles.objects.filter(article_A_la_une= True)[:4]
    derniers = Articles.objects.order_by('date')[:6]
    Categorie = Categories.objects.all()

    data = {
        'article': article,
        'derniers' : derniers,
       'Categorie' : Categorie,
       'art':art
        
        }
        # methode qui nous permet d afficher les articles
    return render(request,'actualites/index.html', data)

def lire(request,id):
    article = get_object_or_404(Articles, id=id)
    
    context = {
        'article':article
    }
    return render(request,'actualites/lire.html',context)


# def send_email(request):
#     nom_contact = request.POST.get('Noms_contact', '')
#     message_object = request.POST.get ('objet_Message','')
#     client_email = request.POST.get('mail', '')
#     message = request.POST.get('message', '')   
#     if Noms_contact and objet_Message and mail and message :
#         try:
#             send_mail(nom_contact, message_object, client_email, message, ['anuaritemathe11@gmail.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('rassurez-vous que tous les champs sont rempli')

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


def Nous_Contacter(request):

    form = ContactForm(request.POST or None)
    
    if request.method == 'POST': 
        
        if form.is_valid():
            Noms = form.cleaned_data['Noms']
            objet_Message = form.cleaned_data ['objet_Message']
            Mail= form.cleaned_data['Mail']
            message = form.cleaned_data['message']
            
            form.save()

            send_mail(Noms, objet_Message, message, Mail, ['anuaritemathe11@gmail.com'], fail_silently=False)
            return redirect('/Nous_Contacter')
        else: 
            form = form_class() # Nous créons un formulaire vide

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
