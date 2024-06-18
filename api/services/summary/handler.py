from api.services.summary.process import SummaryProcess
from common.models.job_offer_model import JobOfferModel
from common.services.generative_ai.generative_ai_factory import GenerativeAIFactory

class SummaryHandler:
  @staticmethod
  def generate(account_id: str, job_offer: JobOfferModel):
    summary = SummaryProcess()
    summary.build_job_offer(job_offer).build_job_experience(account_id)

    repository = GenerativeAIFactory.create()
    return repository.send(summary.prompt)
