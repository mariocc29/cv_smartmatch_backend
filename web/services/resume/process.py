from common.models.job_offer_model import JobOfferModel
from django.utils.translation import gettext as _

class ResumeProcess:

  def __init__(self, job_offer: JobOfferModel, lang: str):
    self.job_offer = job_offer
    self.lang = lang
  
  def format(self):
    self.__build_personal_info()
    self.__build_job_experiences()
    self.__build_educations()
    
    return self.job_offer
  
  def __build_personal_info(self):
    self.job_offer['personal_info']['fullname'] = self.job_offer['personal_info']['fullname'].upper()
    self.job_offer['personal_info']['languages'] = [_(f'personal_info.lang.{self.lang}.{lang}') for lang in self.job_offer['personal_info']['languages']]
    pass

  def __build_job_experiences(self):
    self.job_offer['job_experiences'].sort(key=lambda item: item["start_at"], reverse=True)

  def __build_educations(self):
    self.job_offer['educations'].sort(key=lambda item: item["start_at"], reverse=True)