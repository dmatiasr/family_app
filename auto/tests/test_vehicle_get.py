import json

import pytest
from django.urls import reverse

from auto.models import Automovil

vehicle_url_list = reverse("vehicles-list")


@pytest.mark.django_db
def test_zero_vehicles_should_return_empty_list(client, existing_user) -> None:
    client.force_login(existing_user)
    response = client.get(vehicle_url_list)

    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_one_company_exists_should_succeed(client, existing_user) -> None:
    vehicle = Automovil.objects.create(name="Siena", matricula="IGQ549")
    client.force_login(existing_user)
    response = client.get(vehicle_url_list)

    assert response.status_code == 200
    response = json.loads(response.content)[0]
    assert response.get("name") == vehicle.name
    assert response.get("matricula") == vehicle.matricula

    vehicle.delete()
