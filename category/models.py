from __future__ import unicode_literals

from django.db import models
from base.models import TimeAuditModel
# Create your models here.


class Category(TimeAuditModel):
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,blank=True)
	


	def __str__(self):
		return self.name


class Subcategory(TimeAuditModel):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100,blank=True)
	categoryId = models.ForeignKey(Category,on_delete = models.CASCADE)
	


	def __str__(self):
		return self.name

