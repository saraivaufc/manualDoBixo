from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context

from handbook.models import Topic, Item, Contact
from handbook.forms import ContactForm

PAGE_SIZE = 8

class Index(object):
	def index(self, request, page=1):
		if request.user.groups.filter(name='organizer').exists():
			return HttpResponseRedirect(reverse('handbook:admin_index'))
		context = {}
		context['topics'] =  Topic.objects.all()

		pages = Paginator(Item.objects.order_by('topic'), PAGE_SIZE)
		items = pages.page(page)
		context['pages'] = pages
		context['items'] = items
		context['is_index']=True
		return render(request, 'handbook/index.html',context)
	
	def see_topic(self, request, topic_slug, page=1):
		context = {}
		topics = Topic.objects.all()
		context['topics'] = topics	
		try:
			topic = Topic.objects.get(slug=topic_slug)
			context['topic']=topic
		except Topic.DoesNotExist:
			messages.error(request, _('Topic Not Exists!!!'))
			return HttpResponseRedirect(reverse('handbook:index', kwargs={'page':page}))
		
		pages = Paginator(topic.get_items(), PAGE_SIZE)
		items = pages.page(page)
		context['pages'] = pages
		context['items'] = items
		context['is_index']=True
		return render(request, 'handbook/content/see_topic.html',context)

	def see_item(self, request, topic_slug, item_slug):
		context = {}
		topics = Topic.objects.all()
		context['topics'] = topics	
		try:
			topic = Topic.objects.get(slug=topic_slug)
			context['topic']=topic
		except Topic.DoesNotExist:
			messages.error(request, _('Topic Not Exists!!!'))
			return HttpResponseRedirect(reverse('handbook:index'))
		
		try:
			item = Item.objects.get(slug=item_slug)
			context['item']=item
		except Item.DoesNotExist:
			messages.error(request, _('item Not Exists!!!'))
			return HttpResponseRedirect(reverse('handbook:see_topic', kwargs={'topic_slug':topic_slug}))
		
		return render(request, 'handbook/content/see_item.html',context)

	def contact(self, request):
		context = {}
		if request.method == 'POST':
			form = ContactForm(request.POST)
			if form.is_valid():
				contact = form.save()
				if contact:
					t = loader.get_template('handbook/contact_email.html')
					c = Context({ 'contact': contact})
					text_content = 'This is an important message.'
					rendered = t.render(c)
					msg = EmailMultiAlternatives(_("Manual do Bixo - Contact"), 
													text_content, 
													contact.get_email(), 
													['saraiva.ufc@gmail.com', 'saraiva@alu.ufc.br'],)
					msg.attach_alternative(rendered , "text/html")
					msg.send()
					messages.success(request, _('Suggestion send sucess!!!'))
				else:
					messages.error(request, _('Fail send Suggestion!!!'))
			else:
				messages.error(request, _('Form invalid!!!'))
			return HttpResponseRedirect(reverse('handbook:index')) 
		else:
			form = ContactForm()
			context['form'] = form
		context['is_contact']=True
		return render(request, 'handbook/contact.html', context)

	def about(self, request):
		context = {}
		context['is_about']=True
		return render(request, 'handbook/about.html', context)