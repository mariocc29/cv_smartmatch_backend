from django.urls import path

from web.views.resume_views import ResumePDFView, ResumeDOCView

urlpatterns = [
	path('resume/<str:job_offer_id>.pdf', ResumePDFView.as_view()),
  path('resume/<str:job_offer_id>.docx', ResumeDOCView.as_view()),
]