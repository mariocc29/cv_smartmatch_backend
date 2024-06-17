from django.urls import path

from . import personal_info_views

urlpatterns = [
	path('personal_info/', personal_info_views.personal_infos),
	path('personal_info/<str:personal_info_id>/', personal_info_views.personal_info),
]