from rest_framework.serializers import ModelSerializer
from .models import Items,Stock


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Items
        fields = "__all__"





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


class PurchaseSerailizer(ModelSerializer):
    items=ItemSerializer()
    class Meta:
        model=Items
        field=["id","items","count"]

