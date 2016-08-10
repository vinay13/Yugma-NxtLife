from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
#from accounts.models import Account

# Create your models here.
class Message(models.Model):

	#user = models.ForeignKey(Account, on_delete = models.CASCADE)
	message = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now , db_index = True)


	def __str__(self):
		return self.message

"""

	def __unicode__(self):
		return '[{timestamp}] :{message}'.format(**self.as_dict())


		@property
		def formatted_timestamp(self):
			return self.timestamp.strftime('%b %-d %-I:%M %p')


		@property
		def as_dict(self):
			return {'message':self.message , 'timestamp':self.formatted_timestamp}



"""	