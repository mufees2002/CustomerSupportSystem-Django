import django.http
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import  permissions
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from .models import Items, Stock, Purchase
from .Serializer import (
    ItemSerializer,
    StockSerializer,
    PurchaseSerailizer
)



class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()




    def get_queryset(self):
       i=self.request.query_params.get('id')
       if i :
        return Items.objects.filter(id=i)
       return Items.objects.all()



class StockViewSet(ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get_queryset(self):
       id=self.request.query_params.get('id')
       if id:
           return Stock.objects.filter(id__icontains=id)
       return Stock.objects.all()


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerailizer
    queryset = Purchase.objects.all()










