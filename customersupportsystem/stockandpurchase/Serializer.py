from rest_framework.serializers import ModelSerializer
from .models import Items,Stock,Purchase


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Items
        fields = ['id','name','type','price','manufacturedby','date']





class StockSerializer(ModelSerializer):
    items=ItemSerializer()
    class Meta:
        model = Stock
        fields = ["id","items","count","status"]



    def create(self, validated_data):
        items_data=validated_data.pop('items')
        items=Items.objects.create(**items_data)
        stock=Stock.objects.create(items=items,**validated_data)
        return  stock
    def get_value(self, dictionary):
        if "name" in dictionary:
            return dictionary

class PurchaseSerailizer(ModelSerializer):
    items=ItemSerializer()

    class Meta:
        model = Purchase
        fields = ["id", "items", "count", "status"]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        items = Items.objects.create(**items_data)
        purchase = Purchase.objects.create(items=items, **validated_data)
        return purchase

    def get_value(self, dictionary):
        if "name" in dictionary:
            return dictionary