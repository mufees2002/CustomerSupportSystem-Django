from django.shortcuts import render
from pip._vendor.requests import request
from rest_framework.utils import json
from django.core.serializers import serialize

from .models import Registration,AddEmployee
from .LoginSerializer import RegistrationForm,EmployeeSerializer
import  logging
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
@api_view(['GET'])
def Api_Overview(request):
    return Response('HELLO')


@api_view(['POST'])
def add_user(request):
    user=RegistrationForm(data=request.data)
    if user.is_valid():
        user.save()
        return  Response('Added');
    else:
        return  Response('Error')


@api_view(['GET'])
def get_user(request):
    user=Registration.objects.all()
    serialized_data = serialize("json", user)
    serialized_data = json.loads(serialized_data)


    return Response(serialized_data)




@api_view(['GET'])
def login(request):
    data=json.loads(request.body.decode('utf-8'))
    email=data['Email']
    password=data['Password']
    if email:
     user=Registration.objects.filter(Email=email).values('Email','Password')

     if user:
       u_password=user[0]['Password']
       if u_password==password:
         return HttpResponse("Verified")
       else:
         return HttpResponse("InCorrect Password")
     else:
          return HttpResponse("InCorrect Email")
    else:
        return HttpResponse("Not Given")

@api_view(['POST'])
def addemployess(request):
    add_emp=EmployeeSerializer(data=request.data)
    if add_emp.is_valid():
        add_emp.save()
        return HttpResponse("Saves The Employee")
    else:
        return HttpResponse("Error")


@api_view(['POST'])
def deleteemployees(request):

    emp_name=request['name']
    if emp_name:
     emp_d=AddEmployee.objects.filter(Name=emp_name)
     emp_d.delete()
     return HttpResponse("Deleted")
    else:
     return HttpResponse("Error")




