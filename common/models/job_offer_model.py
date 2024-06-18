import mongoengine
from datetime import datetime
from bson import ObjectId

from common.models.account_model import AccountModel

class JobOfferModel(mongoengine.Document):
  meta = { 'collection': 'job_offers' }

  version = mongoengine.IntField(default=1)
  account = mongoengine.ReferenceField(AccountModel)
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
  
  @staticmethod
  def resume(job_offer_id: str):
    pipeline = [
      { '$match': { '_id': ObjectId(job_offer_id) }}, 
      {
        '$lookup': {
          'from': 'personal_infos', 
          'localField': 'account', 
          'foreignField': 'account_id', 
          'as': 'personal_info'
        }
      }, {
        '$unwind': {
          'path': '$personal_info', 
          'preserveNullAndEmptyArrays': True
        }
      }, {
        '$lookup': {
          'from': 'job_experiences', 
          'localField': 'personal_info._id', 
          'foreignField': 'personal_info', 
          'as': 'job_experiences'
        }
      }, {
        '$lookup': {
          'from': 'educations', 
          'localField': 'personal_info._id', 
          'foreignField': 'personal_info', 
          'as': 'educations'
        }
      }, {
        '$addFields': {
          'personal_info.full_address': {
            '$concat': [
              '$personal_info.address.street_address', 
              ', ', 
              '$personal_info.address.postal_code', 
              ', ', 
              '$personal_info.address.province', 
              ', ', 
              '$personal_info.address.city', 
              ', ', 
              '$personal_info.address.country'
            ]
          }
        }
      }, {
        '$project': {
          '_id': False, 
          'summary': True, 
          'personal_info': {
            'fullname': True, 
            'bachelor_degree': True, 
            'email': True, 
            'phone': True, 
            'full_address': True, 
            'social_networks': True, 
            'languages': True
          }, 
          'job_experiences': {
            '$map': {
              'input': '$job_experiences', 
              'as': 'job_experience', 
              'in': {
                'company': '$$job_experience.company', 
                'role': '$$job_experience.role', 
                'start_at': '$$job_experience.start_at', 
                'start_at_formatted': {
                  '$dateToString': { 'format': '%m/%Y', 'date': '$$job_experience.start_at' }
                }, 
                'end_at': '$$job_experience.end_at', 
                'end_at_formatted': {
                  '$dateToString': { 'format': '%m/%Y', 'date': '$$job_experience.end_at' }
                }, 
                'tags': '$$job_experience.tags', 
                'responsibilities': '$$job_experience.responsibilities'
              }
            }
          }, 
          'educations': {
            'institute': True, 
            'degree': True, 
            'start_at': True, 
            'end_at': True
          }
        }
      }
    ]

    return JobOfferModel.objects.aggregate(pipeline).next()