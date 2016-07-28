from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Poll,Option
from polls.serializers import PollSerializer,OptionSerializer


@api_view(['GET', 'POST'])
def poll_list(request):

    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET','DELETE'])
def poll_detail(request,pk):

    try:
        poll = Poll.object.get(pk=pk)
    except Poll.DoesNotExist:
        return HttpResponse(status=401)


    if request.method == 'GET':
        #polls = Poll.objects.all()
        serializer = PollSerializer(poll,many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        poll.delete()
        return Response(status=400)







