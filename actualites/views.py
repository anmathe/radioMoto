
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect 
from django.forms import ModelForm
from .formulaire import ContactForm
from django.core.mail import BadHeaderError, send_mail
from .models import AproposdeNous_NousContacter
from .models import Articles, Categories, sous_Categories, LesEditions_Francaise, LesEditions_swahili, LesEditions_Kinande, Emissions, AproposdeNous_NotreEquipe, AproposdeNous_laRadio, AproposdeNous_ProjetdAvenir


def index(request):
    article = Articles.objects.all()
    art = list(Articles.objects.values())
    articleSlides= Articles.objects.filter(article_A_la_une= True)[:4]
    derniers = Articles.objects.order_by('date')[:6]

    data = {
        'article': article,
        'derniers' : derniers,
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


def send_email(request):
     nom_contact = request.POST.get('Noms_contact', '')
     message_object = request.POST.get ('objet_Message','')
     client_email = request.POST.get('mail', '')
     message = request.POST.get('message', '')   
     if Noms_contact and objet_Message and mail and message :
         try:
             send_mail(nom_contact, message_object, client_email, message,to= ['anuaritemathe11@gmail.com',])
         except BadHeaderError:
             return HttpResponse('Invalid header found.')
         return HttpResponseRedirect('/contact/thanks/')
     else:
         # In reality we'd use a form class
         # to get proper validation errors.
        return HttpResponse('rassurez-vous que tous les champs sont rempli')

def actualités(request):
    article_actualites = Articles.objects.filter( Categories = 'actualites')
    return render(request,'actualites/actualités.html', {'article': article_actualites})
    

def apropos_de_nous(request):
    template = loader.get_template('actualites/apropos_de_nous.html')
    return HttpResponse(template.render(request=request))
    

def Notre_Equipe(request):
    article_team = AproposdeNous_NotreEquipe.objects.filter( Categories = 'notre Equipe')
    return render(request,'actualites/Notre_Equipe.html', {'Notre Equipe':article_team})


def Française(request):
    audio = LesEditions_Francaise.objects.order_by ('-dateEditions')[:5]
    return render(request,'actualites/Française.html', {'audio': audio})


def Swahili(request):
    audioS = LesEditions_swahili.objects.order_by ('-dateEditions')[:5]
    return render(request,'actualites/Swahili.html', {'audioS': audioS})
    #audioS veut dire audio swahili


def Kinande(request):
    audioK = LesEditions_Kinande.objects.order_by ('-dateEditions')[:5]
    return render(request,'actualites/Kinande.html', {'audioK': audioK})


def Nous_Contacter(request):

    form = ContactForm(request.POST or None)
    
    if request.method == 'POST': 
        
        if form.is_valid():
            noms = form.cleaned_data['Noms_contact']
            objet_Message = form.cleaned_data['objet_Message']
            mail= form.cleaned_data['mail']
            message = form.cleaned_data['message']
            recipient = ['anuaritemathe11@gmail.com',]

            form.save()
            
            send_mail(noms, objet_Message, mail, message, recipient, auth_user=None, auth_password=None, connection=None, html_message=None)
            #send_mail (self, 'Noms', 'objet_Message', 'message', 'Mail',  fail_silently=False)
            return redirect('/Nous_Contacter')
        else: 
            form = form_class() # Nous créons un formulaire vide

    return render(request, 'actualites/Nous_Contacter.html', {'form': form})


def Réligieuse(request):
    articles_religieuse = Articles.objects.filter(sous_Categories_id=11)
    return render(request,'actualites/Réligieuse.html', {'articles religieuse':articles_religieuse})


def santé(request):
    articles_sante = Articles.objects.filter(sous_Categories='Sante')
    return render(request,'actualites/santé.html', {'articles sante':articles_sante})

def Politique(request):
    articles_politique = Articles.objects.filter(sous_Categories='politique')
    return render(request,'actualites/Politique.html', {'articles politique':articles_politique})

def Economique(request):
    articles_economique = Articles.objects.filter(sous_Categories='economique')
    return render(request,'actualites/Economique.html', {'articles economique':articles_economique})


def Autres_Actualites(request):
    articles_autres = Articles.objects.filter(sous_Categories='autres actualites')
    return render(request,'actualites/Autres_Actualites.html', {'articles autres':articles_autres })

def emissions(request):
    article_Emissions = Emissions.objects.filter( Categories = 'emissions')
    return render(request,'actualites/emissions.html', {'LesEmissions':article_Emissions})
    

def Emission_Réligieuse(request):
    template = loader.get_template('actualites/Emission_Réligieuse.html')
    return HttpResponse(template.render(request=request))


def Autres_Emissions(request):
    template = loader.get_template('actualites/Autres_Emissions.html')
    return HttpResponse(template.render(request=request))
