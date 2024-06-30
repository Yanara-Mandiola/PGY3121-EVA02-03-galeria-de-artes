from django.shortcuts import render
from rest_framework import viewsets
from .models import ObraArte
from .serializers import ObraArteSerializer

# Create your views here.

class ObraArteViewSet(viewsets.ModelViewSet):
    queryset = ObraArte.objects.all()
    serializer_class = ObraArteSerializer
