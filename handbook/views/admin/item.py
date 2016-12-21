#-*- encoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib import messages

from handbook.utils.decorators import group_required
from handbook.models import Item as ItemModel
from handbook.models import Topic as TopicModel
from handbook.forms import ItemForm

import json



class Item():

	@method_decorator(group_required('organizer'))
	def see(self, request,topic_slug, item_slug):
		try:
			topic = TopicModel.objects.get(slug =topic_slug)
		except:
			return HttpResponseRedirect(reverse('handbook:admin_index'))

		try:
			item = ItemModel.objects.get(slug = item_slug)
			return render(request, "handbook/admin/item/see.html", 
				{'item': item, 'topic': topic})
		except:
			messages.error(request, _("Item No Exists!!!"))
			return HttpResponseRedirect(reverse('handbook:admin_index'))

	@method_decorator(group_required('organizer'))
	def add(self, request, topic_slug):
		try:
			topic = TopicModel.objects.get(slug =topic_slug)
		except:
			return HttpResponseRedirect(reverse('handbook:admin_index'))
		if request.method == "POST":

			request.POST = request.POST.copy()
			try:
				request.POST['topic'] = topic.id
			except:
				return HttpResponseRedirect(reverse('handbook:admin_index'))
			form = ItemForm(request.POST, request.FILES)
			if form.is_valid():
				try:
					item = form.save(commit=False)
					item.set_topic(topic)
					item.save()
					return HttpResponseRedirect(reverse('handbook:admin_topic_see',kwargs={'topic_slug':item.get_topic().get_slug()} ) )
				except:
					messages.error(request, _("Fail add Item!!!"))
			else:
				messages.error(request, _("Form invalid!!!"))
		else:
			form = ItemForm(instance=ItemModel(topic=topic))
		return render(request, "handbook/admin/item/form.html", 
			{'form': form, 'topic': topic, 'action': 'add'})


	@method_decorator(group_required('organizer'))
	def edit(self, request, topic_slug, item_slug):
		try:
			topic = TopicModel.objects.get(slug =topic_slug)
		except:
			return HttpResponseRedirect(reverse('handbook:admin_index'))

		try:
			item = ItemModel.objects.get(slug = item_slug)
		except:
			messages.error(request, _("Item no exists!!!"))
			return HttpResponseRedirect(reverse('handbook:admin_topic_see', kwargs={'topic_slug': topic_slug}))

		if request.method == "POST":
			form = ItemForm(request.POST, request.FILES , instance=item)
			if form.is_valid():
				try:
					item = form.save()
					messages.success(request, _('Item edit success!!!'))
					return HttpResponseRedirect(reverse('handbook:admin_item_see', 
								kwargs={'topic_slug': topic.get_slug(), 'item_slug': item.get_slug()}))
				except:
					messages.error(request, _('Fail edit item!!!'))
			else:
				messages.error(request, _('Form invalid!!!'))
		else:
			form = ItemForm(instance = item)
		return render(request, "handbook/admin/item/form.html", 
			{'form':form,'topic':topic,'item':item,'action': 'edit'})

	@method_decorator(group_required('organizer'))
	def remove(self, request, topic_slug, item_slug):
		try:
			topic = TopicModel.objects.get(slug =topic_slug)
		except:
			return HttpResponseRedirect(reverse('handbook:admin_index'))
		try:
			item = ItemModel.objects.get(slug = item_slug)
			item.delete()
			return HttpResponseRedirect(reverse('handbook:admin_topic_see',kwargs={'topic_slug':item.get_topic().get_slug()} ) )
		except:
			return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))

	

	@method_decorator(group_required('organizer'))
	def cleanTopicsOfItems(self, request):
		try:
			itens = ItemModel.objects.all()
			for i in itens:
				i.topic.clear()
			print _("Success Clean Topics Of Itens")
			return True
		except:
			print _("Error Clean Topics Of Itens")
			return False

	@method_decorator(group_required('organizer'))
	def sorted(self, request):
		if request.method == 'POST':    
			try:
				items_new_order = json.loads(request.POST['items'])
			except Exception, e:
				print e
				messages.error(request, _("Error sort items"))
				return HttpResponse("500")

			items = ItemModel.objects.all()
			
			try:
				for index, i in enumerate(items_new_order):
					ItemModel.objects.filter(id = i).update(position = index + 1)
				messages.success(request,_("Items success sorted."))
				return HttpResponse("200")
			except Exception, e:
				print e
				messages.error(request,_("Items error sorted."))
		return HttpResponse("500")
		