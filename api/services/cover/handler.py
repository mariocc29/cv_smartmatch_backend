from api.services.cover.process import CoverProcess
from common.models.job_offer_model import JobOfferModel
from common.services.generative_ai.generative_ai_factory import GenerativeAIFactory

class CoverHandler:
  @staticmethod
  def generate(job_offer: JobOfferModel):
    cover = CoverProcess(job_offer)
    cover.build_job_offer()\
      .build_total_years_of_experience()\
      .build_job_experience()
    
    repository = GenerativeAIFactory.create()
    return repository.send(cover.prompt)
