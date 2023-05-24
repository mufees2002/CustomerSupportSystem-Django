from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from .views import DashBoardViewset

router=DefaultRouter()
router.register("DashBoard",DashBoardViewset)
urlpatterns=[
    path('dashboard/',include(router.urls))

]