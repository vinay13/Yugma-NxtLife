from rest_framework import serializers
from polls.models import Poll,Option



class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields='__all__'




class OptionSerializer(serializers.ModelSerializer):
	class meta:
		models = Option
		fields = '__all__'
