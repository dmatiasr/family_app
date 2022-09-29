from rest_framework import serializers

from .models import Automovil


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = ("name", "matricula")
