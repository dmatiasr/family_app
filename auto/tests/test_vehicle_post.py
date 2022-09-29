import json

import pytest
from django.urls import reverse

from auto.models import Automovil


vehicle_url_list = reverse("vehicles-list")


@pytest.mark.django_db
def test_create_vehicle_without_params_should_fail(client, django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    client.force_login(user)

    response = client.post(path=vehicle_url_list)
    content = json.loads(response.content)

    assert response.status_code == 400
    assert content.get("name") == ["This field is required."]
    assert content.get("matricula") == ["This field is required."]


@pytest.mark.django_db
def test_create_repeated_matricula_should_be_fail(client, django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    client.force_login(user)

    name, repeated_matricula = "Siena", "IGQ549"
    vehicle = Automovil.objects.create(name=name, matricula=repeated_matricula)

    response = client.post(
        path=vehicle_url_list, data={"name": name, "matricula": repeated_matricula}
    )

    vehicle.delete()
    assert response.status_code == 400
    assert json.loads(response.content).get("matricula") == [
        "automovil with this matricula already exists."
    ]


@pytest.mark.django_db
def test_creation_is_succeeded(client, django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    client.force_login(user)

    name, matricula = "Siena", "IGQ549"

    response = client.post(
        path=vehicle_url_list, data={"name": name, "matricula": matricula}
    )
    content = json.loads(response.content)
    assert response.status_code == 201
    assert content.get("name") == name
    assert content.get("matricula") == matricula
