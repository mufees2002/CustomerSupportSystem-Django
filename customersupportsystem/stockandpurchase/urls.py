from django.urls import path,include

from .views import ItemViewSet,StockViewSet,PurchaseViewSet
from  rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('items', ItemViewSet)
router.register("stock", StockViewSet)
router.register("purchase",PurchaseViewSet)

urlpatterns=[
 path('items/',include(router.urls)),


]




