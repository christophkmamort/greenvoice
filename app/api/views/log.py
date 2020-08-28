from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.log import ValueLogSerializer
from shop.models.log import ValueLog


class ValueLogViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product log.
    """
    queryset = ValueLog.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created',]
    ordering = ['-created']
    serializer_class = ValueLogSerializer

    def perform_create(self, serializer):
        serializer.save()
