from django.shortcuts import render
from rest_framework import viewsets
from category.models import Category,Subcategory
from category.serialzers import CategorySerializer,SubcategorySerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer




class Subcategory(viewsets.ModelViewSet):
	
	queryset = Subcategory.objects.all()
	serializer_class = SubcategorySerializer





	    