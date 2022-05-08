from rest_framework import serializers
from .models import MusicalMetadata


class MusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalMetadata
        fields = '__all__'