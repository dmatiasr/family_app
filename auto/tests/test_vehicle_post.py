import json

import pytest
from django.urls import reverse


vehicle_url_list = reverse("vehicles-list")


@pytest.mark.django_db
def test_create_vehicle_without_params_should_fail(client, django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    client.force_login(user)

    response = client.post(path=vehicle_url_list)
    content = json.loads(response.content)

    assert response.status_code == 400
    assert content.get("name") == ['This field is required.']
    assert content.get("matricula") == ['This field is required.']