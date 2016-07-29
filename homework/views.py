from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from homework.models import Homework , Subject
from homework.serializers import HomeworkSerializer,SubjectSerializer





@api_view(['GET','POST'])
def subject_list(request):


	if request.method == 'GET':
		subject = Subject.objects.all()
		serializer = SubjectSerializer(subject , many=True)
		return Response(serializer.data)



	elif request.method == 'POST':
		serializer = SubjectSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Respose(serializer.errors , status = status.HTTP_400_BAD_REQUEST)		









@api_view(['GET', 'POST'])
def homework_list(request):

	if request.method == 'GET':
		homework1 = Homework.objects.all()
		serializer = HomeworkSerializer(homework1, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = HomeworkSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET','PUT','DELETE'])
def homework_detail(request,pk):

	try:
		homework2= Homework.objects.get(pk=pk)
	except Homework.DoesNotExist:
		return HttpResponse(status=404)


	if request.method == 'GET':
		serializer = HomeworkSerializer(homework2 , many=True)
		return Response(serializer.data)


	elif request.method == 'PUT':
		serializer = HomeworkSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		homework2.delete()
		return Response(status = 204)


