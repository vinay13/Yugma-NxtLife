from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Poll(models.Model):
	POLL_TYPE =(
		('1','school'),
		('2','standard'),)
	id=models.AutoField(primary_key=True)
	createdAt=models.DateTimeField(auto_now = True)
	expiredAt=models.DateField(blank=True)
	is_active = models.BooleanField(default=True)
	question= models.CharField(max_length=155)
	user = models.CharField(max_length=144)
	poll_type = models.CharField(max_length=1,choices = POLL_TYPE)


	def __str__(self):
		return self.question




class Option(models.Model):
	
	OPTIONS_CHOICES =(
					('1','single'),
					('2','multiple'),
		)
	options = models.CharField(max_length=122)
	options_type = models.CharField(max_length=1,choices=OPTIONS_CHOICES)


	def __str__(self):
		return self.options





"""
class Options(models.Model):
	
	OPTIONS_CHOICES =(
					('1','single'),
					('2','multiple'),
		)
	options = models.CharField(max_length=122)
	options_type = models.CharField(max_length=1,choices=OPTIONS_CHOICES)


	def __str__(self):
		return self.options

"""
