from __future__ import unicode_literals

from django.db import models
from base.models import TimeAuditModel,AuditModel
from base.constants import ComplaintStatus
from category.models import Category 
from simple_history.models import HistoricalRecords


# Create your models here.
class Complaint(AuditModel):

	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=233,blank=True)
	body = models.TextField()
	category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
	against_id = models.CharField(max_length=122,blank=True)
	anonymous = models.BooleanField(default = True)
	closedDate = models.DateField(blank=True)
	assignedTo = models.CharField(max_length=122,blank=True)
	status = models.PositiveSmallIntegerField(choices = ComplaintStatus.CHOICES,
											default = ComplaintStatus.OPEN)
	history = HistoricalRecords(table_name='complaint_history')

	def __str__(self):
		return self.title




class ComplaintComment(models.Model):
	id = models.AutoField(primary_key=True)
	comment = models.TextField()
	#complaintId  = models.ForeignKey(Complaint , on_delete = models.CASCADE)
	employee_id = models.CharField(max_length=1,blank=True)
	parent_id = models.CharField(max_length=2,blank=True)
	history = HistoricalRecords()
	


	def __str__(self):
		return self.comment




