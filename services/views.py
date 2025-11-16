from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Service, Connection, Server, ServerConnection, ServiceStack, ContainerService
from .serializers import (ServiceSerializer, ConnectionSerializer, ServerSerializer, 
                          ServerConnectionSerializer, ServiceStackSerializer, ContainerServiceSerializer)
import yaml


# Create your views here.

def index(request):
    """Render the main visualization page"""
    return render(request, 'index.html')


# New viewsets for hierarchical model
class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing servers (Level 0).
    Supports: list, create, retrieve, update, delete
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    @action(detail=True, methods=['get'])
    def stacks(self, request, pk=None):
        """Get all service stacks for a specific server"""
        server = self.get_object()
        stacks = server.service_stacks.all()
        serializer = ServiceStackSerializer(stacks, many=True)
        return Response(serializer.data)


class ServerConnectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing server connections.
    Supports: list, create, retrieve, update, delete
    """
    queryset = ServerConnection.objects.all()
    serializer_class = ServerConnectionSerializer


class ServiceStackViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing service stacks (Level 1).
    Supports: list, create, retrieve, update, delete
    """
    queryset = ServiceStack.objects.all()
    serializer_class = ServiceStackSerializer

    @action(detail=True, methods=['post'])
    def parse_compose(self, request, pk=None):
        """Parse docker-compose.yml content and create container services"""
        stack = self.get_object()
        compose_content = request.data.get('docker_compose_content', stack.docker_compose_content)
        
        if not compose_content:
            return Response({'error': 'No docker-compose content provided'}, status=400)
        
        try:
            # Parse YAML
            compose_data = yaml.safe_load(compose_content)
            
            # Update stack with compose content
            stack.docker_compose_content = compose_content
            stack.save()
            
            # Delete existing container services for this stack
            stack.container_services.all().delete()
            
            # Create container services
            if 'services' in compose_data:
                for service_name, service_config in compose_data['services'].items():
                    ports = []
                    if 'ports' in service_config:
                        ports = service_config['ports']
                    
                    volumes = []
                    if 'volumes' in service_config:
                        volumes = service_config['volumes']
                    
                    networks = []
                    if 'networks' in service_config:
                        networks = list(service_config['networks']) if isinstance(service_config['networks'], dict) else service_config['networks']
                    
                    depends_on = []
                    if 'depends_on' in service_config:
                        depends_on = list(service_config['depends_on']) if isinstance(service_config['depends_on'], dict) else service_config['depends_on']
                    
                    environment = {}
                    if 'environment' in service_config:
                        env_config = service_config['environment']
                        if isinstance(env_config, dict):
                            environment = env_config
                        elif isinstance(env_config, list):
                            environment = {item.split('=')[0]: item.split('=')[1] if '=' in item else '' for item in env_config}
                    
                    ContainerService.objects.create(
                        stack=stack,
                        service_name=service_name,
                        image=service_config.get('image', ''),
                        ports=ports,
                        volumes=volumes,
                        networks=networks,
                        depends_on=depends_on,
                        environment=environment
                    )
            
            # Return updated stack with container services
            serializer = ServiceStackSerializer(stack)
            return Response(serializer.data)
            
        except yaml.YAMLError as e:
            return Response({'error': f'Invalid YAML: {str(e)}'}, status=400)
        except Exception as e:
            return Response({'error': f'Error parsing compose file: {str(e)}'}, status=500)


class ContainerServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing container services (Level 2).
    Supports: list, create, retrieve, update, delete
    """
    queryset = ContainerService.objects.all()
    serializer_class = ContainerServiceSerializer


# Legacy viewsets for backward compatibility
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

