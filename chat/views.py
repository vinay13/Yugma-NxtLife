import random
import string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from chat.models import Message
from chat.serializers import MessageSerializer
# Create your views here.




@api_view(['GET', 'POST'])
def MessageView(request):

    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







"""
def chat_room(request):


	messages = reversed(room.messages.order_by('timestamp',[:50]))


	return render(request,"chat/room.html",{
		
		'messages' : messages
		})
"""


