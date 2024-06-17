from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers.personal_info_serializer import PersonalInfoSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def personal_infos(request):
  if request.method == 'POST':
    serializer = PersonalInfoSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def personal_info(request, id):
  if request.method == 'GET':
    return Response({'ok': 'show', 'id': id})
  elif request.method in ['PATCH', 'PUT']:
    return Response({'ok': 'update', 'id': id})
  elif request.method == 'DELETE':
    return Response({'ok': 'delete', 'id': id})