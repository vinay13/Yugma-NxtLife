from __future__ import unicode_literals

from django.db import models
from base.models import TimeAuditModel
# Create your models here.


class Suggestion(TimeAuditModel):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=233,blank=True)
	body = models.TextField()
	category_id = models.CharField(max_length=122,blank=True)
	against_id = models.CharField(max_length=122,blank=True)
	anonymous = models.BooleanField(default = True)
	createdDate = models.DateTimeField(auto_now = True)
	closedDate = models.DateTimeField()
	user = models.CharField(max_length=12,blank=True)
	assignedTo = models.CharField(max_length=122,blank=True)
	priority = models.CharField(max_length=10,blank=True)



	def __str__(self):
		return self.title





class SuggestionComment(models.Model):
	id = models.AutoField(primary_key=True)
	comment = models.TextField()
	complaint_id  = models.CharField(max_length=1,blank=True)
	employee_id = models.CharField(max_length=1,blank=True)
	parent_id = models.CharField(max_length=2,blank=True)
	time = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.comment		