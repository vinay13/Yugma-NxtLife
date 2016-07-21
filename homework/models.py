from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Homework(models.Model):

	id = models.AutoField(primary_key=True)
	homework = models.TextField()
	subjectID = models.CharField(max_length=12,blank=True)
	standardId = models.CharField(max_length=12,blank=True)
	createdAt = models.DateTimeField(auto_now=True)
	teacherId=models.CharField(max_length=12,blank=True)
	lastdate = models.DateField(blank=True)



	def __str__(self):
		return self.homework



