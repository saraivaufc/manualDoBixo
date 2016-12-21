from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from handbook.models import Topic, Item
from .serializers import TopicSerializer, TopicSerializerPk, TopicSerializerTitles, ItemSerializer, ItemSerializerPk, ItemSerializerTitles

class TopicList(APIView):
	"""
	List all topics, or create a new topic.
	"""
	def get(self, request, format=None):
		topics = Topic.objects.all()
		serializer = TopicSerializerPk(topics,context={'request': request}, many=True)
		return Response(serializer.data)

	# def post(self, request, format=None):
	# 	serializer = TopicSerializer(data=request.DATA, context={'request': request})
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, pk, format=None):
	# 	topic = self.get_object(pk)
	# 	topic.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)

class TopicListTitles(APIView):
	"""
	List all topics, or create a new topic.
	"""
	def get(self, request, format=None):
		topics = Topic.objects.all()
		serializer = TopicSerializerTitles(topics,context={'request': request}, many=True)
		return Response(serializer.data)


class TopicDetail(APIView):
	"""
	Retrieve, update or delete a topic instance.
	"""
	def get_object(self, pk):
		try:
			return Topic.objects.get(pk=pk)
		except Topic.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		topic = self.get_object(pk)
		topic = TopicSerializer(topic, context={'request': request})
		return Response(topic.data)

	# def put(self, request, pk, format=None):
	# 	topic = self.get_object(pk)
	# 	serializer = TopicSerializer(topic, data=request.DATA, context={'request': request})
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, pk, format=None):
	# 	topic = self.get_object(pk)
	# 	topic.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)


class ItemList(APIView):
	"""
	List all items, or create a new item.
	"""
	def get(self, request, format=None):
		items = Item.objects.all()
		serializer = ItemSerializerPk(items, context={'request': request}, many=True)
		return Response(serializer.data)

	# def post(self, request, format=None):
	# 	serializer = ItemSerializer(data=request.DATA , context={'request': request})
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, pk, format=None):
	# 	item = self.get_object(pk)
	# 	item.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)

class ItemListTitles(APIView):
	"""
	List all items, or create a new item.
	"""
	def get(self, request, format=None):
		items = Item.objects.all()
		serializer = ItemSerializerTitles(items, context={'request': request}, many=True)
		return Response(serializer.data)

class ItemDetail(APIView):
	"""
	Retrieve, update or delete a item instance.
	"""
	def get_object(self, pk):
		try:
			return Item.objects.get(pk=pk)
		except Item.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		item = self.get_object(pk)
		item = ItemSerializer(item, context={'request': request})
		return Response(item.data)

	# def put(self, request, pk, format=None):
	# 	item = self.get_object(pk)
	# 	serializer = ItemSerializer(item, data=request.DATA, context={'request': request})
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, pk, format=None):
	# 	item = self.get_object(pk)
	# 	item.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)