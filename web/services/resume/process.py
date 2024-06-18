from common.models.job_offer_model import JobOfferModel


class ResumeProcess:

  def __init__(self, job_offer: JobOfferModel):
    self.job_offer = job_offer
  
  def format(self):
    self.__build_personal_info()
    self.__build_job_experiences()
    self.__build_educations()
    
    return self.job_offer
  
  def __build_personal_info(self):
    pass

  def __build_job_experiences(self):
    self.job_offer['job_experiences'].sort(key=lambda item: item["start_at"], reverse=True)

  def __build_educations(self):
    self.job_offer['educations'].sort(key=lambda item: item["start_at"], reverse=True)