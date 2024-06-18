import mongoengine
from datetime import datetime

class JobOfferModel(mongoengine.Document):
  meta = { 'collection': 'job_offers' }

  version = mongoengine.IntField(default=1)
  company = mongoengine.StringField(required=True, max_length=255)
  description = mongoengine.StringField(required=True)
  responsibilities = mongoengine.ListField(mongoengine.StringField())
  requirements = mongoengine.ListField(mongoengine.StringField())
  active = mongoengine.BooleanField(default=True)
  contact = mongoengine.StringField(required=False, max_length=255)
  network = mongoengine.StringField(required=True, max_length=255)
  summary = mongoengine.StringField(required=False, allow_null=True, default=None)
  created_at = mongoengine.DateTimeField(default=datetime.now)
  updated_at = mongoengine.DateTimeField(default=datetime.now)
    
  def save(self, *args, **kwargs):
    self.updated_at = datetime.now()
    return super(JobOfferModel, self).save(*args, **kwargs)