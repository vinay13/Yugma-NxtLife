from django.test import TestCase

# Create your tests here.
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from category.models import Category
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient



class ClientLogged(APITestCase):

	def setUp(self):
		#self.client.Create()
		self.client.login(username='vinay', password='omglol123#')


class CategoryTests(ClientLogged):




	def test_create_category(self):
		url = reverse('category-list')
		#key = '62c2c92599fea0cc593dffa3ce190a4f20a1fb9b'
		#header ={'content-type': 'application/json','Authorization': 'Token {}'.format('62c2c92599fea0cc593dffa3ce190a4f20a1fb9b')}
		data = {
			"name" : "dfsdf"

		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Category.objects.count(), 1)
		self.assertEqual(Category.objects.get().name, data['name'])




	# def test_update_category(self):
	# 	url = reverse('category-detail',kwargs={pk=1})
	# 	data = {"name":"fdsggf"}
	# 	response = self.client.put(url,data,format='json')
		#self.assertEqual(response.status_code , status.HTTP_200_CREATED)





