import mongoengine

from common.models.personal_info_model import PersonalInfoModel

class EducationModel(mongoengine.Document):
  meta = { 'collection': 'educations' }

  version = mongoengine.IntField(default=1)
  personal_info = mongoengine.ReferenceField(PersonalInfoModel)
  institute = mongoengine.StringField(required=True, max_length=255)
  degree = mongoengine.StringField(required=True, max_length=255)
  start_at = mongoengine.IntField(required=True)
  end_at = mongoengine.IntField()