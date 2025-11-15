from django.db import models

# Create your models here.

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

