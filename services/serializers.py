from rest_framework import serializers
from .models import Service, Connection


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
