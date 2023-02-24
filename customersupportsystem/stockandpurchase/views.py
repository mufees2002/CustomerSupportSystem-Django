from rest_framework.viewsets import ModelViewSet

from .models import Items, Stock
from .Serializer import (
    ItemSerializer,
    StockSerializer,
)

class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()





class StockViewSet(ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

