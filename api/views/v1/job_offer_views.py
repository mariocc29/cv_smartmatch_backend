from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers.job_offer_serializer import JobOfferSerializer
from common.models.job_offer_model import JobOfferModel

@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
def job_offer(request, job_offer_id:str = None):
  if job_offer_id is None:
    if request.method == 'GET':
      job_offer = JobOfferModel.objects().order_by('-created_at')
      serializer = JobOfferSerializer(job_offer, many=True)
      return Response(serializer.data)
    
    elif request.method == 'POST':
      serializer = JobOfferSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  else:
    try:
      job_offer = JobOfferModel.objects.get(id=job_offer_id)
    except JobOfferModel.DoesNotExist:
      return Response({'error': 'Job offer not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = JobOfferSerializer(job_offer)
      return Response(serializer.data)
    
    elif request.method in ['PATCH', 'PUT']:
      data = request.data
      serializer = JobOfferSerializer(job_offer, data=data, partial=(request.method == 'PATCH'))
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      job_offer.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)