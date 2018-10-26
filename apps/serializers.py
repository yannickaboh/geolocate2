# Ici je prepare mes models a etre serializer ou formater en json
# 
from rest_framework.serializers import  ModelSerializer
from .models import Etablissement


class EtablissementSerializer(ModelSerializer):

	class Meta:
		model = Etablissement
		fields = ['id', 'nom', 'ville', 'quartier', 'repere', 'telephone', 
		'email', 'adresse', 'longitude', 'latitude']
