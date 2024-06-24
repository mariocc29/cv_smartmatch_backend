from django.http import HttpResponse

from web.services.document.components.document_generator import DocumentGenerator


class DOCGenerator(DocumentGenerator):
  def __init__(self, response: HttpResponse):
    self.response = response

  def content_type(self) -> str:
    return 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

  def generate_document(self, rendered_html: str) -> HttpResponse:
    pass