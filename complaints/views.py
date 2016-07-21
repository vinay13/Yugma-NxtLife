from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from complaints.models import Complaint,ComplaintComment
from complaints.serializers import ComplaintSerializer,ComplaintCommentSerializer


@api_view(['GET', 'POST'])
def complaint_list(request):

	if request.method == 'GET':
		complaints = Complaint.objects.all()
		serializer = ComplaintSerializer(complaints, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ComplaintSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def complaint_detail(request,pk):

	try:
		complaint = Complaint.objects.get(pk=pk)
	except Complaint.DoesNotExist:
		return HttpResponse(status=404)


	if request.method == 'GET':
		serializer = ComplaintSerializer(complaint , many=True)
		return Response(serializer.data)


	elif request.method == 'PUT':
		serializer = ComplaintSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		complaint.delete()
		return Response(status = 204)







@api_view(['GET','POST'])
def complaintComment_list(request):
	
	if request.method == 'GET':
		comments = ComplaintComment.objects.all()
		serializer = ComplaintCommentSerializer(comment,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
		serializer = ComplaintComment(data=request.data)	   		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	
			
