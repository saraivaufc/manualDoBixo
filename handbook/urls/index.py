from django.conf.urls import patterns, include, url
from handbook.views import Index, Search

index = Index()
search = Search()

urlpatterns = patterns('',
	url(r'^$', index.index, name="index"),
	url(r'^(?P<page>\d+)/$', index.index, name="index"),

	url(r'^(?P<topic_slug>[\w-]+)/(?P<page>\d+)/$', index.see_topic, name="see_topic"),
	url(r'^(?P<topic_slug>[\w-]+)/(?P<item_slug>[\w-]+)/$', index.see_item, name="see_item"),
	
	url(r'^contact/$', index.contact, name="contact"),
	url(r'^search/$', search.search, name="search"),
	url(r'^about/$', index.about, name="about"),
)
