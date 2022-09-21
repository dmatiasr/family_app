from rest_framework import (
    permissions,
    viewsets,
)

from .models import Automovil
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]