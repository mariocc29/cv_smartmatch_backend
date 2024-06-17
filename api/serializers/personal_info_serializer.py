from rest_framework import serializers

from common.enums.lang_enums import LangEnums
from common.models.personal_info_model import PersonalInfoModel

class AddressSerializer(serializers.Serializer):
    street_address = serializers.CharField(max_length=255)
    postal_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

class PersonalInfoSerializer(serializers.Serializer):
    version = serializers.IntegerField(required=False)
    fullname = serializers.CharField(max_length=255)
    bachelor_degree = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    address = AddressSerializer()
    social_networks = serializers.ListField(required=False)
    preferred_lang = serializers.CharField(max_length=2)
    languages = serializers.ListField()
    
    def validate_preferred_lang(self, value):
        if value not in [lang.value for lang in LangEnums]:
            raise serializers.ValidationError("Invalid language")
        return value
    
    def validate_languages(self, value):
        invalid_languages = [lang for lang in value if lang not in [lang.value for lang in LangEnums]]
        if invalid_languages:
            raise serializers.ValidationError("Invalid languages: {}".format(", ".join(invalid_languages)))
        return value
    
    def create(self, validated_data):
        user = PersonalInfoModel(**validated_data)
        # user.account_id = self.context['request'].user
        user.save()
        return user