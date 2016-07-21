from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,blank=True)
	createdAt = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name


class Subcategory(models.Model):
	id=models.AutoField(primary_key)
	name=models.CharField(max_length=100)
	createdAt = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name

		