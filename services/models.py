from django.db import models

# Create your models here.

# Level 0: Server (outer level)
class Server(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    description = models.TextField(blank=True)
    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"

    class Meta:
        ordering = ['name']


class ServerConnection(models.Model):
    """Represents directional connectivity between servers"""
    source = models.ForeignKey(Server, related_name='outgoing_connections', on_delete=models.CASCADE)
    target = models.ForeignKey(Server, related_name='incoming_connections', on_delete=models.CASCADE)
    is_healthy = models.BooleanField(default=True)  # Green if True, Red if False
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = "healthy" if self.is_healthy else "unhealthy"
        return f"{self.source.name} -> {self.target.name} ({status})"

    class Meta:
        unique_together = ['source', 'target']
        ordering = ['source__name', 'target__name']


# Level 1: Service Stack (Product/docker-compose group)
class ServiceStack(models.Model):
    """Represents a docker-compose stack (product)"""
    server = models.ForeignKey(Server, related_name='service_stacks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    docker_compose_content = models.TextField(blank=True, help_text="Docker compose YAML content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} on {self.server.name}"

    class Meta:
        ordering = ['server__name', 'name']
        unique_together = ['server', 'name']


# Level 2: Container Service (individual service in docker-compose)
class ContainerService(models.Model):
    """Represents an individual service in a docker-compose stack"""
    stack = models.ForeignKey(ServiceStack, related_name='container_services', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    image = models.CharField(max_length=200, blank=True)
    ports = models.JSONField(default=list, help_text="List of exposed ports")
    volumes = models.JSONField(default=list, help_text="List of volumes")
    networks = models.JSONField(default=list, help_text="List of networks")
    depends_on = models.JSONField(default=list, help_text="List of service dependencies")
    environment = models.JSONField(default=dict, help_text="Environment variables")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_name} ({self.stack.name})"

    class Meta:
        ordering = ['stack__name', 'service_name']
        unique_together = ['stack', 'service_name']


# Legacy models for backward compatibility
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=500)
    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Connection(models.Model):
    source = models.ForeignKey(Service, related_name='outgoing_connections', on_delete=models.CASCADE)
    target = models.ForeignKey(Service, related_name='incoming_connections', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source.name} -> {self.target.name}"

    class Meta:
        unique_together = ['source', 'target']
        ordering = ['source__name', 'target__name']

