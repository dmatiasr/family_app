import json

from django.urls import reverse
from rest_framework import status

from auto.models import Automovil


service_url_list = reverse("services-list")


def test_post_unauthenticated_user(client):
    response = client.post(path=service_url_list)
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert content["detail"] == "Authentication credentials were not provided."


def test_create_services_without_params_should_fail(
    client, existing_user, required_field_text
):
    client.force_login(existing_user)

    response = client.post(path=service_url_list)
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert content.get("applied_date") == required_field_text
    assert content.get("description") == required_field_text
    assert content.get("price") == required_field_text


def test_creation_is_succeeded(client, existing_user):
    client.force_login(existing_user)

    vehicle = Automovil.objects.create(name="Siena", matricula="IGQ549")
    service_data = {
        "applied_date": "2022-08-28",
        "name": "Cambio de mangueras",
        "description": "Se hizo la revision y cambio de mangueras",
        "technician": "mazzoni",
        "price": "30000",
        "related_vehicle": "IGQ549",
    }

    response = client.post(path=service_url_list, data=service_data)

    assert response.status_code == status.HTTP_201_CREATED
    content = json.loads(response.content)
    assert content.get("related_vehicle") == service_data.get("related_vehicle")
    assert content.get("applied_date") == service_data.get("applied_date")
    assert content.get("name") == service_data.get("name")
    assert content.get("description") == service_data.get("description")
    assert content.get("technician") == service_data.get("technician")
    assert content.get("price") == service_data.get("price")

    vehicle.delete()
