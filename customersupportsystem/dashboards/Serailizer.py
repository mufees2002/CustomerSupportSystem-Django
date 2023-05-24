from rest_framework import serializers
from .models import Dashboard
from django.apps import apps


class DashboardSerializer(serializers.ModelSerializer):


   class Meta:
        model=Dashboard
        fields='__all__'



 
       


