import pytest


@pytest.fixture(name="existing_user")
@pytest.mark.django_db
def create_authenticated_user(django_user_model):
    uname, passwd = "foo", "bar"
    user = django_user_model.objects.create_user(username=uname, password=passwd)
    return user


@pytest.fixture
def required_field_text():
    return ["This field is required."]
