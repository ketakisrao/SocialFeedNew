from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from socialfeed import views
from .models import Auth
urlpatterns = [
	url(r'^$', views.view, name='view'),
	url(r'api/$', views.AuthList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
