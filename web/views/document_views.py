from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


from common.models.job_offer_model import JobOfferModel
from web.services.document.handler import DocumentHandler
from web.services.resume.handler import ResumeHandler

class DocumentView(GenericAPIView):

  def get(self, request, document_type, format_type, job_offer_id):
    try:
      job_offer = JobOfferModel.resume(job_offer_id)
      lang = request.GET.get('lang', 'en')
      
      response = DocumentHandler.generate(job_offer, document_type, format_type, lang)
      return response
    except (StopIteration, ValueError) as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)