from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

#@python_2_unicode_compatible
class Event(models.Model):
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=123,blank=True)
	body=models.TextField()
	createdDate = models.DateTimeField(db_index=True,auto_now_add=True)
	event_date = models.DateField(auto_now=True)
	start_time = models.TimeField(db_index=True,default="10:00")
	end_time = models.TimeField(default="14:00")
	event_type_id =models.IntegerField(null=True,blank=True)
	event_standard = models.CharField(max_length=128,blank=True)




	def __str__(self):
		return self.title


	