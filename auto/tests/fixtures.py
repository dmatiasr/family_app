import pytest


@pytest.fixture(name="existing_user")
def create_authenticated_user(django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    return user
