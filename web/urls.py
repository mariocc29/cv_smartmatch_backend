from django.urls import path

from web.views.document_views import DocumentView

urlpatterns = [
  path('documents/<str:document_type>/<str:format_type>/<str:job_offer_id>/', DocumentView.as_view())
]