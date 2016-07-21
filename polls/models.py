from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Poll(models.Model):
	id=models.AutoField(primary_key=True)
	createdAt=models.DateTimeField()
	expiredAt=models.DateField()
	is_active = models.BooleanField()
	question= models.CharField(max_length=155)
	user = models.CharField(max_length=144)
	poll_type = models.BooleanField()


	def __str__(self):
		return self.question



class Options(models.Model):
	
	options = models.CharField(max_length=122)


	def __str__(self):
		returns self.options


