from common.models.job_offer_model import JobOfferModel
from common.services.translator.translator_factory import TranslatorFactory
from web.services.resume.process import ResumeProcess

class ResumeHandler:

  @staticmethod
  def data(job_offer: JobOfferModel, lang: str = 'en') -> dict:
    translator_service = TranslatorFactory.create()
    process = ResumeProcess(job_offer, lang, translator_service)
    return process.format()