from rest_framework import serializers

from common.models.account_model import AccountModel

class AccountSerializer(serializers.Serializer):
  version = serializers.IntegerField(required=False)
  email = serializers.EmailField()
  password = serializers.CharField()

  def to_representation(self, instance):
    data = dict()
    data['email'] = instance.email
    return data

  def create(self, validated_data):
    account = AccountModel.objects(email=validated_data.get('email'))
    if len(account) > 0:
        raise Exception('Account already exists')

    password = validated_data.pop('password', None)
    account = AccountModel(**validated_data)
    account.set_password(password)
    account.save()
    return account
  
  def authenticate(self, validated_data):
    account = AccountModel.objects.get(email=validated_data['email'])
    
    if not account:
      raise AccountModel.DoesNotExist
    
    if account.check_password(validated_data['password']) == False:
      raise Exception('Invalid credentials')
    
    return account