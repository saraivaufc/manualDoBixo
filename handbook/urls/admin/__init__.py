from django.conf.urls import patterns, include, url
from handbook.views.admin import Admin

admin = Admin()

urlpatterns = patterns('',
	url(r'^$' , admin.index, name="admin_index"),
	url(r'^topic/', include('handbook.urls.admin.topic')),
	url(r'^item/', include('handbook.urls.admin.item')),
	url(r'^person/', include('handbook.urls.admin.person')),
)
