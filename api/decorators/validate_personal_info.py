from rest_framework.response import Response
from rest_framework import status

from common.models.personal_info_model import PersonalInfoModel

def validate_personal_info(func):
  
  def wrapper(request, personal_info_id, *args, **kwargs):
    try:
      personal_info = PersonalInfoModel.objects.get(id=personal_info_id)
    except PersonalInfoModel.DoesNotExist:
      return Response({'error': 'Personal info not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return func(request, personal_info, *args, **kwargs)
  
  return wrapper