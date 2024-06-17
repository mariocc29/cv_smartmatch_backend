from bson import ObjectId
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

from common.models.account_model import AccountModel

class MongoDBJWTAuthentication(JWTAuthentication):
  def get_user(self, validated_token):
    user_id = validated_token[api_settings.USER_ID_CLAIM]
    try:
      return AccountModel.objects.get(pk=ObjectId(user_id))
    except AccountModel.DoesNotExist:
      return None