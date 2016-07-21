from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Complaint(models.Model):
	STATUS_CHOICES =(
					(0,'open'),
					(1,'closed'),
					(2,'reopen')
					)

	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=233,blank=True)
	body = models.TextField()
	category_id = models.CharField(max_length=122,blank=True)
	against_id = models.CharField(max_length=122,blank=True)
	anonymous = models.BooleanField(defualt = True)
	status = models.CharField(max_length=12,choices=STATUS_CHOICES)
	createdDate = models.DateTime(auto_now = True)
	closedDate = models.DateTime()
	user = models.CharField(max_length=12,blank=True)
	assignedTo = models.CharField(max_length=122,blank=True)





	def __str__(self):
		return self.title




class ComplaintComment(models.Model):
	id = models.AutoField(primary_key=True)
	comment = models.TextField()
	complaint_id  = models.CharField(max_length=1,blank=True)
	employee_id = models.CharField(max_length=1,blank=True)
	parent_id = models.CharField(max_length=2,blank=True)
	time = models.DateTime(auto_now=True)


	def __str__(self):
		return self.comment




