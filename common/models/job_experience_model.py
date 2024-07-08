import mongoengine

from common.models.personal_info_model import PersonalInfoModel

class JobExperienceModel(mongoengine.Document):
  meta = { 'collection': 'job_experiences' }

  version = mongoengine.IntField(default=1)
  personal_info = mongoengine.ReferenceField(PersonalInfoModel)
  company = mongoengine.StringField(required=True, max_length=255)
  description = mongoengine.StringField(required=True)
  role = mongoengine.StringField(required=True, max_length=255)
  start_at = mongoengine.DateField(required=True)
  end_at = mongoengine.DateField()
  tags = mongoengine.ListField(mongoengine.StringField(max_length=255))
  responsibilities = mongoengine.ListField(mongoengine.StringField())