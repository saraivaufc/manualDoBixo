from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings

urlpatterns = patterns('',
	url(r'^', include('handbook.urls', namespace="handbook", app_name="handbook")),
	url(r'^api/', include('handbook.api.urls')),
	#url(r'^admin_django/$', include(admin.site.urls), name='admin_django'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)



if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if 'social.apps.django_app.default':
    urlpatterns += patterns('',
        url('', include('social.apps.django_app.urls', namespace='social')),
    )




#ERRORS

def handler404(request):
    response = render_to_response('handbook/status/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('handbook/status/500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
