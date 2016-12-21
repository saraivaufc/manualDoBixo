from django.conf.urls import patterns, include, url
from handbook.views.admin import Person

person = Person() 

urlpatterns = patterns('',
	url(r'^$', person.see_admins, name='see_admins'),
	url(r'^admins/$', person.see_admins, name='see_admins'),
	url(r'^admins_removed/$', person.see_admins_removed, name='see_admins_removed'),
	url(r'^remove_admin/(?P<person_id>\d+)/$', person.remove_admin, name='remove_admin'),
	url(r'^restore_admin/(?P<person_id>\d+)/$', person.restore_admin, name='restore_admin'),
	url(r'^keys/$', person.see_access_keys, name='see_access_keys'),
	url(r'^remove_access_key/(?P<access_key_id>\d+)/$', person.remove_access_key, name='remove_access_key'),
)