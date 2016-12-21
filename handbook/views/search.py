#-*-  encoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from handbook.models import Topic, Item
import string
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Search():
	def search(self, request):
		if request.method == "POST":
			search = request.POST['search']

			#verify if is topic
			topics = Topic.objects.filter(title = search)
			if len(topics) > 0:
				topic = topics[0]
				return HttpResponseRedirect(reverse('handbook:see_topic', kwargs={'topic_slug':topic.get_slug(), 'page':1}))

			#verify if is item
			items = Item.objects.filter(title = search)
			if len(items) > 0:
				item = items[0]
				return HttpResponseRedirect(reverse('handbook:see_item', kwargs={'topic_slug':item.get_topic().get_slug(), 'item_slug':item.get_slug()}))


			search = self.filterString(search)
			items = Item.objects.all()
			itemsCount = {}
			for i in items:
				itemsCount[i.id] = self.searchWeight(i.description, search)
			maxItemCount = max(itemsCount.values())

			print itemsCount
			if maxItemCount == 0:
				messages.warning(request, _("Results no Found!!!"))
				return HttpResponseRedirect(reverse('handbook:index'))
			try:
				id = None
				for key, value in itemsCount.items():
					if value == maxItemCount:
						id = key

				item = Item.objects.get(id = id)
				searchResult = search

				return HttpResponseRedirect(reverse('handbook:see_item', kwargs={'topic_slug':item.get_topic.get_slug(), 'item_slug':item.get_slug()}))

			except:
				return HttpResponseRedirect(reverse('handbook:index'))

		else:
			return HttpResponseRedirect(reverse('handbook:index'))


	def filterString(self, text):
		text = text.upper()
		textFilter = text.split(" ")
		textFilter = self.minimizeStringList(textFilter, 3)
		textFilter = self.excludePronoums(textFilter)
		textFilter = self.concatStringList(textFilter)
		return textFilter

	def searchWeight(self, text, phrase):
		text = text.upper()
		phrase = phrase.upper()
		return self.myCount(text, phrase)

	def myCount(self, text, phrase):
		strings =  phrase.split(' ')
		strings = self.minimizeStringList(strings, 3)
		strings = self.excludePronoums(strings)
		if len(strings) == 0:
			return 0
		elif len(strings) == 1:
			return string.count(text, strings[0]) * len(strings[0])
		else:
			counts = map( lambda x:  string.count(text, x) * len(x), strings)
			return sum(counts)

	def minimizeStringList(self, stringList, min_size):
		return filter(lambda x : len(x) >= min_size , stringList)

	def concatStringList(self, stringList):
		if len(stringList) == 0:
			return ""
		elif len(stringList) == 1:
			return stringList[0]
		else:
			return  reduce(lambda x, y : x + " " + y, stringList)


	def excludePronoums(self, stringList):
		dic =['PARA', 'COMO','NAO', "SIM"]

		return filter(lambda x :  len( filter(lambda y :  x == y,  dic )  ) == 0  , stringList)