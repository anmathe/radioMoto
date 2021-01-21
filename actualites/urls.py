from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
   url(r'^index', views.index),
   url(r'^noseditions', views.noseditions),
   url(r'^emissions', views.emissions),
   url(r'^actualités', views.actualités),
   url(r'^apropos_de_nous', views.apropos_de_nous),
   url(r'^La_Radio', views.La_Radio),
   url(r'^Notre_Equipe', views.Notre_Equipe),
   url(r'^Projet_d_Avenir', views.Projet_d_Avenir),
   url(r'^Nous_Contacter', views.Nous_Contacter),
   url(r'^Réligieuse', views.Réligieuse),
   url(r'^santé', views.santé),
   url(r'^Politique', views.Politique),
   url(r'^Economique', views.Economique),
   url(r'^Autres_Actualites', views.Autres_Actualites),
   url(r'^Emission_Réligieuse', views.Emission_Réligieuse),
   url(r'^Autres_Emissions', views.Autres_Emissions),
   url(r'^Française', views.Française),
   url(r'^Kinande', views.Kinande),
   url(r'^Swahili', views.Swahili),
   url(r'^search/$', views.search),

]