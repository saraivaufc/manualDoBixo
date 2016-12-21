from django.conf.urls import patterns, include, url
from handbook.views.admin import Topic

topic = Topic() 

urlpatterns = patterns('',
	url(r'^see_all/$' , topic.see_all, name="admin_topic_see_all"),
	url(r'^see/(?P<topic_slug>[\w-]+)/$' , topic.see, name="admin_topic_see"),
	url(r'^add/$' , topic.add, name="admin_topic_add"),
	url(r'^remove/(?P<topic_slug>[\w-]+)/$' , topic.remove, name="admin_topic_remove"),
	url(r'^edit/(?P<topic_slug>[\w-]+)/$' , topic.edit, name="admin_topic_edit"),
	url(r'^sorted/$' , topic.sorted, name="admin_topic_sorted"),
)