import pytest
import json
from unittest import TestCase

from django.urls import reverse
from django.test import Client


class TestGetVehicles(TestCase):
    
    def test_zero_vehicles_should_return_empty_list(self) -> None:
        client = Client()
        url = reverse("vehicles-list")
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.load(response.content), [])