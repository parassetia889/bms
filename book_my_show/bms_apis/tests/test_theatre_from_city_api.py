import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .setup import SetUp


class TestTheatreFromCityAPI(TestCase):

    def test_theatre_from_city_api(self):
        SetUp.setup()
        user = User.objects.get(username='lauren')
        client = APIClient()
        client.force_authenticate(user=user)
        resp = client.get('/api/get_theatre_from_city/', {'name': 'hyderabad'})
        self.assertEqual(json.loads(resp.content), {'Theatres': ['Icon Hitech']})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
