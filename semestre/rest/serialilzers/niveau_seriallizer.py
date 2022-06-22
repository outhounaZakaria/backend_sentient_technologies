from rest_framework import serializers
from semestre.models import Niveau 

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ["nom_niveau", "type_niveau", "filiere"]