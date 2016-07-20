from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=123,blank=True)
	body=models.CharField(max_length=255,blank=True)
	createdDate = models.DateTimeField(auto_now_add=True)
	event_date = models.DateField(auto_now=True)
	event_time = models.CharField(max_length=50,blank=True)
	event_type_id =models.IntegerField(blank=True)
	event_standard = models.CharField(max_length=128,blank=True)




	def __str__(self):
		self.title


	