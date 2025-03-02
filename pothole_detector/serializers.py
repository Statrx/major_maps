from rest_framework import serializers
from .models import Pothole

class PotholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pothole
        fields = ['latitude', 'longitude', 'severity']

