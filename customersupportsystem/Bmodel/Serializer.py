from rest_framework import serializers
from .models import  Setup


class SetupSerializer(serializers.Serializer):
    class Meta:
        model=Setup
        fields='__all__'