from django.urls import path,include

from .views import ItemViewSet,StockViewSet
from  rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("items", ItemViewSet)
router.register("stock", StockViewSet)

urlpatterns=[
 path('items/',include(router.urls))
]

