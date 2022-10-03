import json

from django.urls import reverse
from rest_framework import status
import pytest

from auto.models import (
    Automovil,
    Service,
)


service_url_list = reverse("services-list")


def test_get_unauthenticated_user(client):
    response = client.get(path=service_url_list)
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert content["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_zero_vehicles_should_return_empty_list(client, existing_user) -> None:
    client.force_login(existing_user)
    response = client.get(service_url_list)

    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_one_service_exist_should_succeed(client, existing_user):

    vehicle = Automovil.objects.create(name="Siena 1.4", matricula="IGQ549")
    service_data = {
        "applied_date": "2022-08-26",
        "name": "Revision y cambio de mangueras",
        "description": "Se hizo la revision y cambio de mangueras",
        "technician": "Mazzoni",
        "price": "30000",
        "related_vehicle": vehicle,
    }
    service = Service.objects.create(**service_data)

    client.force_login(existing_user)
    response = client.get(service_url_list)
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content.get("related_vehicle") == vehicle.matricula
    assert content.get("applied_date") == service_data.get("applied_date")
    assert content.get("name") == service_data.get("name")
    assert content.get("description") == service_data.get("description")
    assert content.get("technician") == service_data.get("technician")
    assert content.get("price") == service_data.get("price")

    vehicle.delete()
    service.delete()
