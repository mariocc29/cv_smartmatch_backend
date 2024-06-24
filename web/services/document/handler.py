from common.models.job_offer_model import JobOfferModel
from web.services.document.process import DocumentProcess


class DocumentHandler:

  @staticmethod
  def generate(job_offer: JobOfferModel, document_type: str, format_type: str, lang: str):
    process = DocumentProcess(document_type, format_type, lang)
    return process.generate_document(job_offer)