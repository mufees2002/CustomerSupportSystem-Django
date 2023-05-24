from django.shortcuts import render,HttpResponse

from rest_framework.viewsets import ModelViewSet
from .models import Dashboard
from .Serailizer import DashboardSerializer

class DashBoardViewset(ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()