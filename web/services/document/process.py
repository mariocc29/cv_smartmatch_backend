from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.translation import activate

from common.models.job_offer_model import JobOfferModel
from web.services.document.components.document_factory import DocumentFactory
from web.services.resume.handler import ResumeHandler


class DocumentProcess:
  def __init__(self, document_type: str, format_type: str, lang: str):
    self.document_type = document_type
    self.format_type = format_type
    self.lang = lang
  
  def prepare_data(self, job_offer: JobOfferModel) -> dict:
    activate(self.lang)
    return ResumeHandler.data(job_offer, self.lang)

  def render_template(self, data: dict) -> str:
    template = get_template(f"{self.document_type}.html")
    return template.render(data)

  def generate_document(self, job_offer: JobOfferModel) -> HttpResponse:
    document_data = self.prepare_data(job_offer)
    rendered_html = self.render_template(document_data)

    response = HttpResponse()
    generator = DocumentFactory.create_generator(response, format_type=self.format_type)
    generator.generate_document(rendered_html)

    response['Content-Type'] = generator.content_type
    response['Content-Disposition'] = f'attachment; filename="{job_offer['personal_info']['fullname']}.{self.format_type}"'

    return response