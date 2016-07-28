import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from polls.models import Poll




class ClientLogged(APITestCase):

    def setUp(self):
		self.client.login(username='tushar', password='tushar@123')


class PollTests(ClientLogged):

    def test_create_poll(self):

    	#myToken = '62c2c92599fea0cc593dffa3ce190a4f20a1fb9b'
        url = reverse('poll-list')
        header ={'content-type': 'application/json',
           'Authorization': 'Token 62c2c92599fea0cc593dffa3ce190a4f20a1fb9b'}
        data = {
            "question": "fgdhsgfg",
            "user": "vinay",
            "poll_type": "2",
            "option_id" : "1"

        }
        response = self.client.post(url,header, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(Poll.objects.get().question, data['question'])