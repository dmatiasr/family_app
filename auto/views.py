from rest_framework import (
    permissions,
    viewsets,
)
from rest_framework.response import Response

from .models import (
    Automovil,
    Service,
)
from .serializers import (
    VehicleSerializer,
    ServiceSerializer,
)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.prefetch_related("related_vehicle")
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
