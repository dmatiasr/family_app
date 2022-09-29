import json

from django.urls import reverse
from rest_framework import status

from auto.models import Automovil


vehicle_url_list = reverse("vehicles-list")


def test_create_vehicle_without_params_should_fail(client, existing_user):
    client.force_login(existing_user)

    response = client.post(path=vehicle_url_list)
    content = json.loads(response.content)

    required_fields = ["This field is required."]

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert content.get("name") == required_fields
    assert content.get("matricula") == required_fields


def test_create_repeated_matricula_should_be_fail(client, existing_user):
    client.force_login(existing_user)

    name, repeated_matricula = "Siena", "IGQ549"
    vehicle = Automovil.objects.create(name=name, matricula=repeated_matricula)

    response = client.post(
        path=vehicle_url_list, data={"name": name, "matricula": repeated_matricula}
    )

    vehicle.delete()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert json.loads(response.content).get("matricula") == [
        "automovil with this matricula already exists."
    ]


def test_creation_is_succeeded(client, existing_user):
    client.force_login(existing_user)

    name, matricula = "Siena", "IGQ549"

    response = client.post(
        path=vehicle_url_list, data={"name": name, "matricula": matricula}
    )
    content = json.loads(response.content)
    assert response.status_code == status.HTTP_201_CREATED
    assert content.get("name") == name
    assert content.get("matricula") == matricula
