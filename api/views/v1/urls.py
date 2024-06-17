from django.urls import path

from . import authentication_views
from . import personal_info_views
from . import job_experience_views
from . import education_views
from . import job_offer_views

urlpatterns = [

  path('auth/sign_in', authentication_views.sign_in),
  path('auth/login', authentication_views.login),
  path('auth/refresh_token', authentication_views.refresh_token),

	path('personal_info/', personal_info_views.personal_info),
	path('personal_info/<str:personal_info_id>/', personal_info_views.personal_info),
  
  path('job_experience/<str:personal_info_id>/', job_experience_views.job_experience),
  path('job_experience/<str:personal_info_id>/<str:job_experience_id>/', job_experience_views.job_experience),
  
  path('education/<str:personal_info_id>/', education_views.education),
  path('education/<str:personal_info_id>/<str:education_id>/', education_views.education),
  
  path('job_offer/', job_offer_views.job_offer),
  path('job_offer/<str:job_offer_id>/', job_offer_views.job_offer),
  path('job_offer/<str:job_offer_id>/summary', job_offer_views.summary),
]