from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from handbook.models import Topic, Item


class TopicSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Topic
		fields = ('id','position', 'title', 'slug', 'creation')

class TopicSerializerPk(TopicSerializer):
	class Meta(TopicSerializer.Meta):
		fields = ('id', 'slug', 'items')

class TopicSerializerTitles(TopicSerializer):
	class Meta(TopicSerializer.Meta):
		fields = ('title', )


class ItemSerializer(serializers.HyperlinkedModelSerializer):
	topic =  TopicSerializer()
	image = VersatileImageFieldSerializer(
       		sizes=[
           	('small', 'thumbnail__128x72'),
            	('medium', 'thumbnail__384x216'),
            	('larger', 'thumbnail__640x360'),
            	('extra_larger', 'thumbnail__896x504'),

            	('full_size', 'url'),
            	#('larger', 'crop__50x50')
        	]
    	)
	class Meta:
		image = serializers.ImageField(use_url=True, allow_empty_file=True)
		model = Item
		fields = ('id', 'position', 'topic','title', 'slug', 'description', 'image', 'creation')

class ItemSerializerPk(ItemSerializer):
	class Meta(ItemSerializer.Meta):
		fields = ('id', 'slug')

class ItemSerializerTitles(ItemSerializer):
	class Meta(ItemSerializer.Meta):
		fields = ('title', )
