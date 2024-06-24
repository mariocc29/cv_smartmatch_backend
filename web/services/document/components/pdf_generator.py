from django.http import HttpResponse
from xhtml2pdf import pisa

from web.services.document.components.document_generator import DocumentGenerator


class PDFGenerator(DocumentGenerator):

  def __init__(self, response: HttpResponse):
    self.response = response
  
  def content_type(self) -> str:
    return 'application/pdf'

  def generate_document(self, rendered_html: str) -> HttpResponse:
    pisa_status = pisa.CreatePDF(rendered_html, dest=self.response, encoding='utf-8')
    
    if pisa_status.err:
      raise ValueError("Error generating PDF")
    
    return self.response
    
