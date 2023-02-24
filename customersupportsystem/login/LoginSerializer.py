from  django import  forms
from rest_framework import serializers
from .models import Registration,AddEmployee




class RegistrationForm(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields="__all__"





class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model=AddEmployee
        fields="__all__"




