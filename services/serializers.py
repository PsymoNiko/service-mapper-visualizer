from rest_framework import serializers
from .models import Service, Connection, Server, ServerConnection, ServiceStack, ContainerService


# New serializers for hierarchical model
class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['id', 'name', 'ip_address', 'description', 'x_position', 'y_position', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ServerConnectionSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='source.name', read_only=True)
    target_name = serializers.CharField(source='target.name', read_only=True)
    source_ip = serializers.CharField(source='source.ip_address', read_only=True)
    target_ip = serializers.CharField(source='target.ip_address', read_only=True)

    class Meta:
        model = ServerConnection
        fields = ['id', 'source', 'target', 'source_name', 'target_name', 
                  'source_ip', 'target_ip', 'is_healthy', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        if data['source'] == data['target']:
            raise serializers.ValidationError("A server cannot connect to itself")
        return data


class ContainerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerService
        fields = ['id', 'stack', 'service_name', 'image', 'ports', 'volumes', 
                  'networks', 'depends_on', 'environment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ServiceStackSerializer(serializers.ModelSerializer):
    container_services = ContainerServiceSerializer(many=True, read_only=True)
    server_name = serializers.CharField(source='server.name', read_only=True)

    class Meta:
        model = ServiceStack
        fields = ['id', 'server', 'server_name', 'name', 'url', 'description', 
                  'docker_compose_content', 'container_services', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


# Legacy serializers for backward compatibility
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'url', 'x_position', 'y_position', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ConnectionSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='source.name', read_only=True)
    target_name = serializers.CharField(source='target.name', read_only=True)

    class Meta:
        model = Connection
        fields = ['id', 'source', 'target', 'source_name', 'target_name', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        if data['source'] == data['target']:
            raise serializers.ValidationError("A service cannot connect to itself")
        return data
