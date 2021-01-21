
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Articles,Categories, sous_Categories


def index(request):
    article = Articles.objects.all()
    return render(request,'actualites/index.html', {'article': article})


# Create your views here.template = loader.get_template('actualites/index.html')
