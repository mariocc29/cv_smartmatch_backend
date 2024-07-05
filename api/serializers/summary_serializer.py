from rest_framework import serializers

from api.mixins.job_offer_url_mixin import JobOfferURLMixin
from common.models.job_offer_model import JobOfferModel

class SummarySerializer(serializers.Serializer, JobOfferURLMixin):
  id = serializers.CharField(read_only=True)
  summary = serializers.CharField()
  url = serializers.SerializerMethodField()

  def update(self, instance: JobOfferModel, validated_data):
    instance.summary = validated_data['summary']
    instance.save()
    return instance