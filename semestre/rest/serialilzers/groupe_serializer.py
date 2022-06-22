from rest_framework import serializers
from semestre.models import Groupe 

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = ["nom_group", "niveau"]