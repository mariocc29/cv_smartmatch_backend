from rest_framework import serializers

from common.models.job_offer_model import JobOfferModel

class SummarySerializer(serializers.Serializer):
  id = serializers.CharField(read_only=True)
  summary = serializers.CharField()

  def update(self, instance: JobOfferModel, validated_data):
    instance.summary = validated_data['summary']
    instance.save()
    return instance