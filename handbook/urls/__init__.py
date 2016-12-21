from django.conf.urls import patterns, include, url
from handbook.views import *
from handbook.views.admin import *


urlpatterns = patterns('',
	url(r'^$', include('handbook.urls.index')),
	url(r'^index/', include('handbook.urls.index')),
	url(r'^admin/', include('handbook.urls.admin')),
	url(r'^accounts/', include('handbook.urls.accounts')),
)
