from django.test import TestCase

# Create your tests here.
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from events.models import Event




class ClientLogged(APITestCase):

    def setUp(self):
		self.client.login(username='vinay', password='omglol123#')


class EventTests(ClientLogged):

    def test_create_event(self):

    	#myToken = '62c2c92599fea0cc593dffa3ce190a4f20a1fb9b'
        url = reverse('event-list')
        # header ={'content-type': 'application/json',
        #    'Authorization': 'Token 62c2c92599fea0cc593dffa3ce190a4f20a1fb9b'}
        data = {
            "title": "Curriculam",
            "body" : "random bodyyyy"

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, data['title'])