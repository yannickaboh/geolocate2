# Ici fichier de routage de apps pas du projet MapSchool
# lors de la creation d'une application django ne cree pas ce fichier 
# donc c'est au programmeur de le faire y compris tous les autres fichiers 
# tel ke serializers.py, forms.py, filters.py ....etc.

from django.conf.urls import url, include
from django.contrib import admin

# Importation des fichiers views.py models.py et serializers.py
from apps import views
from apps import models
from apps import serializers

#definition d'un namespace(petit nom de mon application)
app_name = 'apps'


urlpatterns = [
	
	# Chargement des urls du site d'administration depuis mon appli apps
	url(r'^admin/', admin.site.urls),

	# Les routes de mon API
	# Pour mieux comprendre la syntaxe des urls, il faut savoir ke la partie de gauche 
	# Affichera l'url ke l'utilisateur verra sur son navigateur
	# La partie du milieu indik la vue de traitement correspondant dans le fichier views.py
	# lapartie de droite s'il yen a indik juste le nom ke l'on a choisit de donner 
	# a notre url afin ke l'on puisse pouvoir pointer dessus comme avec un lien
	# Exemple: <a href="{% url 'apps:admin' %}">Aller à la page d'amin</a>
	# Cette route affichera la liste des ets
	url(r'^api/etablissement/$', views.EtablissementList.as_view()),
	# ?P<pk>\d+) cet expression reguliere pemret d'afficher l'identifiant correspodant
	# Exemple: api/ets/1/ ou api/ets/101
	# La route suivante affichera les details d'un ets
    url(r'^api/etablissement/(?P<pk>\d+)/$', views.EtablissementDetailList.as_view()),



]
