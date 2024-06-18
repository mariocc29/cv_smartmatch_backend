from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from xhtml2pdf import pisa

from common.models.job_offer_model import JobOfferModel
from web.services.resume.handler import ResumeHandler

class ResumePDFView(GenericAPIView):

  def get(self, request, *args, **kwargs):
    try:
      job_offer = JobOfferModel.resume(kwargs['job_offer_id'])
    except StopIteration:
      # return redirect('error_view_name')
      return Response({'error': 'Job offer not found'}, status=status.HTTP_404_NOT_FOUND)
    
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="{job_offer['personal_info']['fullname']}.pdf"'
    response['Content-Disposition'] = f'filename="{job_offer['personal_info']['fullname']}.pdf"'

    template = get_template('resume.html')
    html = template.render(ResumeHandler.data(job_offer))
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')

    if pisa_status.err:
      return HttpResponse({'error': 'Error generating PDF'}, status=500)
    
    return response