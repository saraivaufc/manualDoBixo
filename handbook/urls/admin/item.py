from django.conf.urls import patterns, include, url
from handbook.views.admin import Item

item = Item()

urlpatterns = patterns('',
	url(r'^see/(?P<topic_slug>[\w-]+)/(?P<item_slug>[\w-]+)/$' , item.see, name="admin_item_see"),
	url(r'^add/(?P<topic_slug>[\w-]+)/$' , item.add, name="admin_item_add"),
	url(r'^remove/(?P<topic_slug>[\w-]+)/(?P<item_slug>[\w-]+)/$' , item.remove, name="admin_item_remove"),
	url(r'^edit/(?P<topic_slug>[\w-]+)/(?P<item_slug>[\w-]+)/$' , item.edit, name="admin_item_edit"),
	url(r'^sorted/(?P<topic_slug>[\w-]+)/$' ,item.sorted, name="admin_item_sorted"),
)