from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from handbook.utils.decorators import group_required
from django.utils.decorators import method_decorator


class Admin():	
	@method_decorator(group_required('organizer'))
	def index(self, request):
		return HttpResponseRedirect(reverse('handbook:admin_topic_see_all'))
