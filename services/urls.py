from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ConnectionViewSet, index

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'connections', ConnectionViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
