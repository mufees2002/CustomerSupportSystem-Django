from django.urls import path,include

from . import views
urlpatterns=[
    path('/Bsetup',views.Add_BSetup)
]