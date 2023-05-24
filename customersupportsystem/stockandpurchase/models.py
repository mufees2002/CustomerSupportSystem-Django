
from django.db import models

class Items(models.Model):


    name = models.CharField(max_length=32)
    type=models.CharField(max_length=32)
    price=models.IntegerField(default=0)
    manufacturedby=models.CharField(max_length=32)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Stock(models.Model):
     items= models.ForeignKey(
        Items,
        related_name="items",
        on_delete=models.CASCADE,null=True,blank=True)
     count=models.IntegerField(default=0)
     status = models.CharField(max_length=32,default="UNSOLD")


class Purchase(models.Model):
    items=models.ForeignKey(
        Items,
        related_name="pitems",
        on_delete=models.CASCADE)
    count=models.IntegerField(default=0)
    status=models.CharField(max_length=32,default="SOLD")