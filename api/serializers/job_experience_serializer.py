from rest_framework import serializers

from common.models.job_experience_model import JobExperienceModel

class JobExperienceSerializer(serializers.Serializer):
  id = serializers.CharField(read_only=True)
  version = serializers.IntegerField(required=False)
  company = serializers.CharField(max_length=255)
  description = serializers.CharField()
  role = serializers.CharField(max_length=255)
  start_at = serializers.DateField()
  end_at = serializers.DateField(required=False, allow_null=True)
  tags = serializers.ListField(child=serializers.CharField())
  responsibilities = serializers.ListField(child=serializers.CharField())

  def create(self, validated_data):
    job_experience = JobExperienceModel(**validated_data)
    job_experience.personal_info = self.context['personal_info']
    job_experience.save()
    return job_experience
  
  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    
    instance.save()
    return instance