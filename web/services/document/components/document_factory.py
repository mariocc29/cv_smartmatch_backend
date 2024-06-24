from django.http import HttpResponse

from web.services.document.components.doc_generator import DOCGenerator
from web.services.document.components.pdf_generator import PDFGenerator


class DocumentFactory:

  @staticmethod
  def create_generator(response: HttpResponse, format_type: str):
    if format_type == 'pdf':
      return PDFGenerator(response)
    elif format_type == 'doc':
      return DOCGenerator(response)
    else:
      raise ValueError("Invalid format type")