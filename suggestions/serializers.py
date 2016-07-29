from rest_framework import serializers
from suggestions.models import Suggestion,SuggestionComment




class SuggestionSerializers(serializers.ModelSerializer):
	Model = Suggestion
	fields ='__all__'


class SuggestionCommentSerializer(serializers.ModelSerializer):
	Model = SuggestionComment
	fields = '__all__'
