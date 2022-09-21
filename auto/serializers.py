from rest_framework import serializers

from .models import Automovil


class VehicleSerializer(serializers.Serializer):
    class Meta:
        model = Automovil
        fields = ("name", "matricula")
