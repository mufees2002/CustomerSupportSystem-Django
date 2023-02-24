from django.db import models

# Create your models here.


class Setup(models.Model):
    Name=models.CharField(max_length=200,default="SOME STRING")
    Type=models.CharField(max_length=200,default="SOME STRING")
    Country=models.CharField(max_length=200,default="India")
    State=models.CharField(max_length=200,default="Tamil Nadu")
    Location=models.CharField(max_length=200,default="xxxx")
    Currency=models.CharField(max_length=200,default="Rupee")
    Profit=models.CharField(max_length=200,default="1000")
    File=models.FileField
