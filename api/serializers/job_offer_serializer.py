from rest_framework import serializers

from api.mixins.job_offer_url_mixin import JobOfferURLMixin
from common.models.job_offer_model import JobOfferModel

class JobOfferSerializer(serializers.Serializer, JobOfferURLMixin):
  id = serializers.CharField(read_only=True)
  version = serializers.IntegerField(required=False)
  company = serializers.CharField(max_length=255)
  description = serializers.CharField()
  position = serializers.CharField()
  responsibilities = serializers.ListField(child=serializers.CharField())
  requirements = serializers.ListField(child=serializers.CharField())
  active = serializers.BooleanField(required=False)
  contact = serializers.CharField(required=False, allow_null=True, max_length=255)
  network = serializers.CharField(max_length=255)
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  url = serializers.SerializerMethodField()

  def create(self, validated_data):
    job_offer = JobOfferModel(**validated_data)
    job_offer.account = self.context['request'].user
    job_offer.save()
    return job_offer
  
  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    
    instance.save()
    return instance