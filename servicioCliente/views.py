from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import PQR, Soporte
from .serializer import SoporteSerializer, PQRSerializer

class SoporteListCreate(generics.ListCreateAPIView):
    # Soporte.objects.all() = select * from soportes, object para acceder al ORM
    queryset = Soporte.objects.all()
    serializers_class = SoporteSerializer

class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializers_class = SoporteSerializer
    
class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializers_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializers_class = PQRSerializer