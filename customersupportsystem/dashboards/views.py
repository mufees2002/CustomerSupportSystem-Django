from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Dashboard
from .Serailizer import DashboardSerializer

class Dasboard(ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()


