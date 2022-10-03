from rest_framework import serializers

from .models import (
    Automovil,
    Service,
)


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = ("name", "matricula")


class ServiceSerializer(serializers.ModelSerializer):
    related_vehicle = serializers.SlugRelatedField(
        slug_field="matricula", queryset=Automovil.objects.all()
    )

    class Meta:
        model = Service
        fields = (
            "related_vehicle",
            "applied_date",
            "name",
            "description",
            "technician",
            "price",
        )
