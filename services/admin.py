from django.contrib import admin
from .models import Service, Connection


# Register your models here.

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

