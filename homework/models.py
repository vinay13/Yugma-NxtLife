from __future__ import unicode_literals

from django.db import models
from base.models import TimeAuditModel
# Create your models here.



class Subject(models.Model):

	id = models.AutoField(primary_key = True)
	subject = models.CharField(max_length = 120 , blank = True)



	def __str__(self):
		return self.subject









class Homework(TimeAuditModel):

	id = models.AutoField(primary_key=True)
	homework = models.TextField()
	subjectID = models.ForeignKey(Subject , on_delete = models.CASCADE)
	standardId = models.CharField(max_length=12,blank=True)
	teacherId=models.CharField(max_length=12,blank=True)
	lastdate = models.DateField(blank=True)



	def __str__(self):
		return self.homework



