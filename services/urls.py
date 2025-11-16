from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ServiceViewSet, ConnectionViewSet, index, ServerViewSet, 
                    ServerConnectionViewSet, ServiceStackViewSet, ContainerServiceViewSet)

router = DefaultRouter()
# New hierarchical endpoints
router.register(r'servers', ServerViewSet)
router.register(r'server-connections', ServerConnectionViewSet)
router.register(r'stacks', ServiceStackViewSet)
router.register(r'container-services', ContainerServiceViewSet)

# Legacy endpoints for backward compatibility
router.register(r'services', ServiceViewSet)
router.register(r'connections', ConnectionViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
