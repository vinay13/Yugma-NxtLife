from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from base.models import TimeAuditModel , AuditModel
from base.constants import EventType 
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

#@python_2_unicode_compatible

"""
class EventType(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 120 , blank=True)
	color = models.CharField(max_length=20 , blank=True)

	def __str__(self):
		return self.name
"""



class Event(TimeAuditModel):
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=123,blank=True)
	body=models.TextField()
	event_date = models.CharField(max_length=40,blank=True)
	start_time = models.TimeField(db_index=True,default="10:00")
	end_time = models.TimeField(default="14:00")
	event_type = models.PositiveSmallIntegerField(choices = EventType.CHOICES, default = EventType.SCHOOL )
	event_standard = models.CharField(max_length=128,blank=True)




	def __str__(self):
		return self.title


	