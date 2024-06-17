from django.urls import path

from . import personal_info_views
from . import job_experience_views
from . import education_views

urlpatterns = [
	path('personal_info/', personal_info_views.personal_info),
	path('personal_info/<str:personal_info_id>/', personal_info_views.personal_info),
  path('job_experience/<str:personal_info_id>/', job_experience_views.job_experience),
  path('job_experience/<str:personal_info_id>/<str:job_experience_id>/', job_experience_views.job_experience),
  path('education/<str:personal_info_id>/', education_views.education),
  path('education/<str:personal_info_id>/<str:education_id>/', education_views.education),
]