from django.conf.urls import patterns, url
from .views import TopicList, TopicListTitles, TopicDetail, ItemList, ItemListTitles, ItemDetail


urlpatterns = patterns(
	'handbook.api.views',
    url(r'^topics/$', TopicList.as_view(), name='topics_list'),
    url(r'^topics_titles/$', TopicListTitles.as_view(), name='topics_list_titles'),
    url(r'^topics/(?P<pk>[0-9]+)$', TopicDetail.as_view(), name='topics_detail'),
    url(r'^items/$', ItemList.as_view(), name='items_list'),
    url(r'^items_titles/$', ItemListTitles.as_view(), name='items_list_titles'),
    url(r'^items/(?P<pk>[0-9]+)$', ItemDetail.as_view(), name='items_detail'),

    # url(r'^items/$', 'items_list', name='items_list'),
    # url(r'^items/(?P<pk>[0-9]+)$', 'items_detail', name='items_detail'),
)