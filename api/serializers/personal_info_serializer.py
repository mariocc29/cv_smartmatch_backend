from rest_framework import serializers

from common.enums.lang_enums import LangEnums
from common.models.personal_info_model import Address, PersonalInfoModel, SocialNetwork

class AddressSerializer(serializers.Serializer):
    street_address = serializers.CharField(max_length=255)
    postal_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

class SocialNetworkSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=255)
    url = serializers.URLField()

class LangEnumField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        kwargs['choices'] = [lang.value for lang in LangEnums]
        super().__init__(**kwargs)

    def to_representation(self, obj):
        if isinstance(obj, LangEnums):
            return obj.value
        return obj

    def to_internal_value(self, data):
        try:
            return LangEnums(data)
        except ValueError:
            self.fail('invalid_choice', input=data)

class PersonalInfoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    version = serializers.IntegerField(required=False)
    fullname = serializers.CharField(max_length=255)
    bachelor_degree = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    address = AddressSerializer()
    social_networks = SocialNetworkSerializer(many=True, required=False)
    preferred_lang = LangEnumField()
    languages = serializers.ListField(child=LangEnumField())
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        social_networks_data = validated_data.pop('social_networks', [])
        address = Address(**address_data)
        social_networks = [SocialNetwork(**sn) for sn in social_networks_data]
        personal_information = PersonalInfoModel(**validated_data, address=address, social_networks=social_networks)
        # personal_information.account_id = self.context['request'].user
        personal_information.save()
        return personal_information
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        social_networks_data = validated_data.pop('social_networks', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)

        if social_networks_data:
            instance.social_networks = [SocialNetwork(**sn) for sn in social_networks_data]

        instance.save()
        return instance