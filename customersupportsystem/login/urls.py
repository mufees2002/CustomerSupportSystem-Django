from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns=[

    path('/',views.Api_Overview),
    path('AddAdmin/',views.add_user),
    path('list/',views.get_user),
    path('login/',views.login),
    path('AddEmployee/ ',views.AddEmployee)

]