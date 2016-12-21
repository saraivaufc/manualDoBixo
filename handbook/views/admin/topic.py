from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from handbook.utils.decorators import group_required
from django.utils.decorators import method_decorator
import json

from handbook.models import Topic as TopicModel
from handbook.forms import TopicForm

from .item import Item



class Topic():	
	def __init__(self):
		self.__item = Item()
	@method_decorator(group_required('organizer'))
	def see_all(self, request):
		if request.method == 'POST':
			return self.sorted(request)
		topics = TopicModel.objects.all()
		return  render(request, "handbook/admin/topic/see_all.html", {'topics': topics})

	@method_decorator(group_required('organizer'))
	def see(self, request, topic_slug):
		if request.method == 'POST':
			return self.__item.sorted(request)
		try:
			topic = TopicModel.objects.get(slug=topic_slug)
		except:
			return HttpResponseRedirect(reverse('handbook:admin_index'))
		return render(request, "handbook/admin/topic/see.html", {'topic': topic})

	@method_decorator(group_required('organizer'))
	def add(self, request):
		if request.method == "POST":
			form = TopicForm(request.POST)
			if form.is_valid():
				if form.save():
					messages.success(request,_("Topic add sucess!!!") )
					return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))
				else:
					messages.error(request, _("Fail add Topic!!!") )
			else:
				messages.error(request,_("Form invalid!!!"))
		else:
			form = TopicForm()
		return render(request, "handbook/admin/topic/form.html", {'form': form, 'action': 'add'})

	@method_decorator(group_required('organizer'))
	def edit(self, request,topic_slug):
		try:
			topic = TopicModel.objects.get(slug = topic_slug)
		except:
			messages.error(request, _("(Topic No Exists!!!"))
			return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))

		if request.method == "POST":
			form = TopicForm(request.POST, instance=topic)
			if form.is_valid():
				if form.save():
					messages.success(request, _("Topic edit sucess!!!"))
					return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))
				else:
					messages.error(request, _("Fail edit Topic!!!"))
			else:
				messages.error(request, _("Form invalid!!!"))
		else:
			form = TopicForm(instance = topic)
		return render(request, "handbook/admin/topic/form.html", 
				{'form': form,'topic' : topic, 'action': 'edit'})

	@method_decorator(group_required('organizer'))
	def remove(self, request,topic_slug):
		try:
		 	topic = TopicModel.objects.get(slug = topic_slug)
			topic.delete()
		except:
			messages.error(request, _("Error remove topic!!!"))
		return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))

	@method_decorator(group_required('organizer'))
	def sorted(self, request):
		if request.method == 'POST':    
			try:
				topics_new_order = json.loads(request.POST['topics'])
			except Exception, e:
				print e
				return HttpResponse("500")

			topics = TopicModel.objects.all()
			
			try:
				for index, i in enumerate(topics_new_order):
					TopicModel.objects.filter(id = i).update(position = index + 1)
				messages.success(request,_("Topics success sorted."))
				return HttpResponse("200")
			except Exception, e:
				print e
				messages.error(request,_("Topics error sorted."))
		return HttpResponse("500")
		