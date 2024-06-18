from common.models.job_offer_model import JobOfferModel
from web.services.resume.process import ResumeProcess

class ResumeHandler:

  @staticmethod
  def data(job_offer: JobOfferModel) -> dict:
    process = ResumeProcess(job_offer)
    return process.format()