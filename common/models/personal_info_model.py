import mongoengine

from common.enums.lang_enums import LangEnums
# from common.models.account_model import AccountModel

class SocialNetwork(mongoengine.EmbeddedDocument):
    label = mongoengine.StringField()
    url = mongoengine.StringField()

class Address(mongoengine.EmbeddedDocument):
    street_address = mongoengine.StringField()
    postal_code = mongoengine.StringField()
    province = mongoengine.StringField()
    city = mongoengine.StringField()
    country = mongoengine.StringField()

class PersonalInfoModel(mongoengine.Document):
    meta = { 'collection': 'personal_infos' }

    version = mongoengine.IntField(default=1)
    # account_id = mongoengine.ReferenceField(AccountModel, unique=True)
    fullname = mongoengine.StringField(required=True, max_length=255)
    bachelor_degree = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    phone = mongoengine.StringField(required=True, max_length=20)
    address = mongoengine.EmbeddedDocumentField(Address)
    social_networks = mongoengine.EmbeddedDocumentListField(SocialNetwork)
    preferred_lang = mongoengine.EnumField(LangEnums)
    languages = mongoengine.ListField(mongoengine.EnumField(LangEnums))
  