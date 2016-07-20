from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from rest_framework.response import Response
from events.models import Event
from events.serializers import EventSerializer


class JSONResponse(HttpResponse):
   
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def event_list(request):
	if request.method == 'GET':
		events = Event.objects.all()
		serializer = EventSerializer(events,many=True)
		return JSONResponse(serializer.data)



	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = EventSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data,status=status.HTTP_201_CREATED)
		return JSONResponse(serializer.data,status=status.HTTP_400_BAD_REQUEST)	



@csrf_exempt
def event_detail(request, pk):

    try:
        events = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(events)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(events, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        events.delete()
        return HttpResponse(status=204)