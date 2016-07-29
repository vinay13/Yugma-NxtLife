from rest_framework import serializers
from homework.models import Homework , Subject



class SubjectSerializer(serializers.ModelSerializer):
	class Meta :
		model = Subject
		fields = '__all__'



class HomeworkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Homework
		fields='__all__'




