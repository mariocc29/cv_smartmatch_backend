from django.urls import include, path

urlpatterns = [
	path('v1/', include('api.views.v1.urls')),
]