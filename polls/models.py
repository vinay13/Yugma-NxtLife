from __future__ import unicode_literals

from django.db import models
from base.models import AuditModel
# Create your models here.



class Poll(AuditModel):

	id=models.AutoField(primary_key=True)
	expiredAt=models.DateField(blank=True)
	is_active = models.BooleanField(default=True)
	question= models.CharField(max_length=155)
	poll_type = models.PositveSmallIntegerField(choices = PollType.CHOICES ,default=PollType.SCHOOL)
	option_id = models.CharField(max_length=2,blank=True)
	
	def __str__(self):
		return self.question




class Option(models.Model):
	
	options = models.CharField(max_length=122)
	options_type = models.PositveSmallIntegerField(choices = PollTOptions.CHOICES ,default=PollOptions.SINGLE)


	def __str__(self):
		return self.options


