from __future__ import unicode_literals

from django.db import models
from base.models import AuditModel
from base.constants import PollType,PollOptions
# Create your models here.




class Option(models.Model):

	id = models.AutoField(primary_key = True)
	options = models.CharField(max_length=122)
	options_type = models.PositiveSmallIntegerField(choices = PollOptions.CHOICES ,default=PollOptions.SINGLE)


	def __str__(self):
		return self.options





class Poll(AuditModel):

	id=models.AutoField(primary_key=True)
	expiredAt=models.DateField(blank=True)
	is_active = models.BooleanField(default=True)
	question= models.CharField(max_length=155)
	poll_type = models.PositiveSmallIntegerField(choices = PollType.CHOICES ,default=PollType.SCHOOL)
	option_id = models.ForeignKey(Option, on_delete = models.CASCADE)
	def __str__(self):
		return self.question







