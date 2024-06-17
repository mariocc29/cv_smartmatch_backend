from rest_framework import serializers

from common.models.education_model import EducationModel

class EducationSerializer(serializers.Serializer):
  id = serializers.CharField(read_only=True)
  version = serializers.IntegerField(required=False)
  institute = serializers.CharField(max_length=255)
  degree = serializers.CharField(max_length=255)
  start_at = serializers.IntegerField()
  end_at = serializers.IntegerField(required=False, allow_null=True)

  def create(self, validated_data):
    education = EducationModel(**validated_data)
    education.personal_info = self.context['personal_info']
    education.save()
    return education
  
  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    
    instance.save()
    return instance