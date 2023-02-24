from django.db import models


# Create your models here.
from django.db.models import Model


class Registration(models.Model):
   Firstname=models.CharField(max_length=200, default='SOME STRING')
   Lastname=models.CharField(max_length=200, default='SOME STRING')
   DOB=models.CharField(max_length=200,default="SOME STRING")
   Email=models.EmailField( default='SOME STRING')
   Phone_Number=models.IntegerField(default=12221111221)
   Password=models.CharField(max_length=200, default='SOME STRING')


   def __str__(self) -> str:
      return  self.Firstname


class AddEmployee(models.Model):
   Name=models.CharField(max_length=200,default='SOME STRING')
   EmailID=models.EmailField(default="No EmailID")
   Level=models.CharField(max_length=200,default="Labour")
   Phone_Number=models.IntegerField(default=0000000000)
   Attendance=models.IntegerField(default=100)





