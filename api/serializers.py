from rest_framework import serializers
from .models import ObraArte

class ObraArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObraArte
        fields = '__all__'
