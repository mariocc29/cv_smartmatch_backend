from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from api.decorators.validate_personal_info import validate_personal_info
from api.serializers.job_experience_serializer import JobExperienceSerializer
from common.models.job_experience_model import JobExperienceModel
from common.models.personal_info_model import PersonalInfoModel

@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
@validate_personal_info
def job_experience(request, personal_info, job_experience_id:str = None):
  if job_experience_id is None:
    if request.method == 'GET':
      job_experiences = JobExperienceModel.objects(personal_info=personal_info).order_by('-start_at')
      serializer = JobExperienceSerializer(job_experiences, many=True)
      return Response(serializer.data)
    
    elif request.method == 'POST':
      serializer = JobExperienceSerializer(data=request.data, context={'personal_info': personal_info})
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  else:
    try:
      job_experience = JobExperienceModel.objects.get(id=job_experience_id)
    except JobExperienceModel.DoesNotExist:
      return Response({'error': 'Job experience not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = JobExperienceSerializer(job_experience)
      return Response(serializer.data)
    
    elif request.method in ['PATCH', 'PUT']:
      data = request.data
      serializer = JobExperienceSerializer(job_experience, data=data, partial=(request.method == 'PATCH'))
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      job_experience.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)