from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.decorators.validate_personal_info import validate_personal_info
from api.serializers.education_serializer import EducationSerializer
from common.models.education_model import EducationModel

@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
@validate_personal_info
def education(request, personal_info:str, education_id:str = None):
  if education_id is None:
    if request.method == 'GET':
      educations = EducationModel.objects(personal_info=personal_info).order_by('-start_at')
      serializer = EducationSerializer(educations, many=True)
      return Response(serializer.data)
    
    elif request.method == 'POST':
      serializer = EducationSerializer(data=request.data, context={'personal_info': personal_info})
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  else:
    try:
      education = EducationModel.objects.get(id=education_id)
    except EducationModel.DoesNotExist:
      return Response({'error': 'Job experience not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = EducationSerializer(education)
      return Response(serializer.data)
    
    elif request.method in ['PATCH', 'PUT']:
      data = request.data
      serializer = EducationSerializer(education, data=data, partial=(request.method == 'PATCH'))
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      education.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)