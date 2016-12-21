from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from handbook.utils.decorators import group_required
from django.utils.decorators import method_decorator

from handbook.models import Person as PersonModel
from handbook.models import Organizer as OrganizerModel
from handbook.models import OrganizerKey


class Person():  
	@method_decorator(group_required('organizer'))
	def see_admins(self, request):
		admins = []
		for person in PersonModel.objects.filter(is_active=True):
			print person, person.get_groups()
			if person.groups.filter(name='organizer').exists():
				admins.append(person)
		return render(request, 'handbook/admin/person/see_admins.html', {'admins': admins,'is_admins': True})

	@method_decorator(group_required('organizer'))
	def see_admins_removed(self, request):
		admins = []
		for person in PersonModel.objects.filter(is_active=False):
			print person, person.get_groups()
			if person.groups.filter(name='organizer').exists():
				admins.append(person)
		return render(request, 'handbook/admin/person/see_admins.html', {'admins': admins,'is_admins': True, 'is_removed':True})

	@method_decorator(group_required('organizer'))
	def see_access_keys(self, request):
		new_register_key = None
		register_keys = None
		if request.method == "POST":
			new_register_key =  OrganizerKey.objects.create(creator=request.user)
		register_keys = OrganizerKey.objects.filter(exists = True)
	
		return render(request, "handbook/admin/person/see_access_keys.html", 
			{'request':request, 'new_register_key': new_register_key ,'register_keys': register_keys})

	def remove_access_key(self, request, access_key_id):
		try:
			access_key = OrganizerKey.objects.get(id = access_key_id)
		except:
			messages.error(request, _("Access Key no exists!!!"))
			return HttpResponseRedirect(reverse('handbook:see_access_keys'))

		if not access_key.in_use:
			access_key.delete()
		else:
			messages.warning(request, _("Erro remove access key!!!"))
		return HttpResponseRedirect(reverse('handbook:see_access_keys'))
	
	def remove_admin(self, request, person_id):
		try:
			person = PersonModel.objects.get(id = person_id)
		except:
			messages.error(request, _("Person no exists!!!"))
			return HttpResponseRedirect(reverse('handbook:see_admins'))
		person.delete()
		messages.success(request,_("User successfully removed!!!"))
		return HttpResponseRedirect(reverse('handbook:see_admins'))
	
	def restore_admin(self, request, person_id):
		try:
			person = PersonModel.objects.get(id = person_id)
		except:
			messages.error(request, _("Person no exists!!!"))
			return HttpResponseRedirect(reverse('handbook:see_admins'))
		person.restore()
		messages.success(request,_("User successfully restore!!!"))
		return HttpResponseRedirect(reverse('handbook:see_admins'))