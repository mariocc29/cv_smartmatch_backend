from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers.personal_info_serializer import PersonalInfoSerializer
from common.models.personal_info_model import PersonalInfoModel

@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
def personal_info(request, personal_info_id:str = None):
  if request.method == 'POST':
    serializer = PersonalInfoSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  else:
    try:
      personal_info = PersonalInfoModel.objects.get(id=personal_info_id)
    except PersonalInfoModel.DoesNotExist:
      return Response({'error': 'Personal info not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = PersonalInfoSerializer(personal_info)
      return Response(serializer.data)
    
    elif request.method in ['PATCH', 'PUT']:
      data = request.data
      serializer = PersonalInfoSerializer(personal_info, data=data, partial=(request.method == 'PATCH'))
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      personal_info.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
