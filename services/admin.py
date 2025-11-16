from django.contrib import admin
from .models import Service, Connection, Server, ServerConnection, ServiceStack, ContainerService


# Register your models here.

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip_address', 'description', 'created_at']
    search_fields = ['name', 'ip_address', 'description']
    list_filter = ['created_at']


@admin.register(ServerConnection)
class ServerConnectionAdmin(admin.ModelAdmin):
    list_display = ['source', 'target', 'is_healthy', 'created_at']
    list_filter = ['is_healthy', 'created_at']
    search_fields = ['source__name', 'target__name']


@admin.register(ServiceStack)
class ServiceStackAdmin(admin.ModelAdmin):
    list_display = ['name', 'server', 'url', 'created_at']
    search_fields = ['name', 'server__name', 'url']
    list_filter = ['server', 'created_at']


@admin.register(ContainerService)
class ContainerServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'stack', 'image', 'created_at']
    search_fields = ['service_name', 'stack__name', 'image']
    list_filter = ['stack', 'created_at']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'x_position', 'y_position', 'created_at']
    search_fields = ['name', 'url']
    list_filter = ['created_at']


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['source', 'target', 'created_at']
    list_filter = ['created_at']
    search_fields = ['source__name', 'target__name']

