from django.db import models
# Create your models here.



class Dashboard(models.Model):


    Name=models.CharField(max_length=32,default=None)
    Price=models.IntegerField(default=0)
    Count=models.IntegerField(default=0)






