from rest_framework import serializers

from api.mixins.job_offer_url_mixin import JobOfferURLMixin
from common.models.job_offer_model import JobOfferModel

class CoverSerializer(serializers.Serializer, JobOfferURLMixin):
  id = serializers.CharField(read_only=True)
  cover = serializers.CharField()
  url = serializers.SerializerMethodField()

  def update(self, instance: JobOfferModel, validated_data):
    instance.cover = validated_data['cover']
    instance.save()
    return instance