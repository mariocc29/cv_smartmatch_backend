from api.services.summary.process import SummaryProcess
from common.models.job_offer_model import JobOfferModel
from common.services.generative_ai.generative_ai_factory import GenerativeAIFactory

class SummaryHandler:
  @staticmethod
  def generate(job_offer: JobOfferModel):
    summary = SummaryProcess(job_offer)
    summary.build_job_offer()\
      .build_total_years_of_experience()\
      .build_job_experience()
    
    repository = GenerativeAIFactory.create()
    return repository.send(summary.prompt)
