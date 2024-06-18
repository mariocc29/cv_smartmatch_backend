from django.urls import path

from web.views.resume_views import ResumePDFView

urlpatterns = [
	path('resume/<str:job_offer_id>', ResumePDFView.as_view()),
]