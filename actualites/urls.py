from django.conf.urls import url

from . import views 


urlpatterns = [
   url(r'^index', views.index),
   url(r'^emissions', views.emissions),
   url(r'^actualités', views.actualités),
   url(r'^apropos_de_nous', views.apropos_de_nous),
   url(r'^Notre_Equipe', views.Notre_Equipe),
   url(r'^Nous_Contacter', views.Nous_Contacter, name = 'Nous_Contacter'),
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
   url('articles/(?P<id>\d+)$', views.lire, name = 'lire'),

]