from django.shortcuts import render
from rest_framework.utils import json
from django.core.serializers import serialize
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.http import HttpResponse
from .models import  Setup
from  .Serializer import SetupSerializer
@api_view(['POST'])
def Add_BSetup(request):
     bsetup=SetupSerializer(data=request.data)
     if b.is_valid():
         b.save()
         HttpResponse("Setup Successfully Saved")
     else:
         HttpResponse("Error")
