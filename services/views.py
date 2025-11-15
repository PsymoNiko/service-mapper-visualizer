from django.shortcuts import render
from rest_framework import viewsets
from .models import Service, Connection
from .serializers import ServiceSerializer, ConnectionSerializer


# Create your views here.

def index(request):
    """Render the main visualization page"""
    return render(request, 'index.html')


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing services.
    Supports: list, create, retrieve, update, delete
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ConnectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing connections between services.
    Supports: list, create, retrieve, update, delete
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

