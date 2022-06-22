from rest_framework import serializers
from semestre.models import Semestre 

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = ["libelle_semestre", "niveau"]