import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .setup import SetUp


class TestMovieFromTheatre(TestCase):

    def test_movie_from_theatre_api(self):
        SetUp.setup()
        user = User.objects.get(username='lauren')
        client = APIClient()
        client.force_authenticate(user=user)
        resp = client.get('/api/get_movie_from_theatre/', {'name': 'icon hitech'})
        self.assertEqual(json.loads(resp.content), {'Movie Names': ['Bahubali']})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
