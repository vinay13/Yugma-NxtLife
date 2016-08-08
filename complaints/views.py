from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from complaints.models import Complaint,ComplaintComment
from complaints.serializers import ComplaintSerializer,ComplaintCommentSerializer



class ComplaintList(APIView):

	def get(self,request,format=None):
		complaints = Complaint.objects.all()
		serializer = ComplaintSerializer(complaints, many=True)
		return Response(serializer.data)
	

	def post(self,request,format=None):
		serializer = ComplaintSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def complaint_detail(request,pk):

	try:
		complaint3 = Complaint.objects.get(pk=pk)

	except Complaint.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		serializer = ComplaintSerializer(complaint3)
		return Response(serializer.data)


	elif request.method == 'PUT':
		serializer = ComplaintSerializer(complaint3,data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		complaint3.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)







@api_view(['GET','POST'])
def complaintComment_list(request):
	
	if request.method == 'GET':
		comments = ComplaintComment.objects.all()
		serializer = ComplaintCommentSerializer(comments,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
		serializer = ComplaintComment(data=request.data)	   		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	
			
