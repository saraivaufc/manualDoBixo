from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from handbook.forms.accounts import LoginForm, RegisterForm, GeneralRegisterForm, OrganizerRegisterForm, ProfileForm
from handbook.management.permissions import group_permissions
from handbook.views.index import Index
from handbook.models import RegisterKey, OrganizerKey, Organizer, Person
from handbook.utils.decorators import group_required


class Accounts(object):
	def __init__(self):
		self.index = Index()
	def login(self, request):
		try:
			if request.method == 'GET': next = request.GET['next']
			else:
				next = None
		except:
			next = None

		if request.user.is_authenticated():
			if next:
				return HttpResponseRedirect(next)
			else:
				return HttpResponseRedirect(reverse('handbook:index'))

		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
				if user and user.is_active:
					try:
						login_user(request, user)
						return HttpResponseRedirect(reverse('handbook:index'))
					except Exception, e:
						messages.error(request, _("Email or password incorrect."))
				else:
					messages.error(request, _("User no exists."))
			else:
				messages.error(request, _("Form no valid"))
		else:
			form = LoginForm()
		return render(request, 'handbook/accounts/login.html', {'form': form})

	def logout(self, request):
		try:
			auth_logout(request)
		except Exception, e:
			print e
		return HttpResponseRedirect(reverse('handbook:login'))

	def register(self, request):
		if request.method == 'POST':
			group = request.POST['group']
			if group in group_permissions:
				key = None
				if group == 'general':
					form = GeneralRegisterForm(request.POST, request.FILES)
				elif group == 'organizer':
					form = OrganizerRegisterForm(request.POST, request.FILES)
					if form.is_valid():
						try:
							key = OrganizerKey.objects.get(key=form.cleaned_data['key'], exists=True, in_use=False)
						except OrganizerKey.DoesNotExist:
							messages.error(request, _("Key no found"))
							return render(request, 'handbook/accounts/register.html', {'form': form})
				else:
					messages.error(request, _("Group not found."))      

				if form.is_valid():
					person = form.save(commit=False)
					try:
						person.set_password(person.password)
						person.save(group=group)
						if key:
							key.add_person(person)
						messages.success(request, _("User created success."))
						email = person.get_email()
						password = request.POST['password']
						request.method = 'POST'
						return self.login(request)
					except Exception, e:
						print e
						messages.error(request, _("Created user error."))
				else:
					messages.error(request, _("Form no valid"))
			else:
				messages.error(request, _("Group not found."))
		else:
			form = RegisterForm()
		return render(request, 'handbook/accounts/register.html', {'form': form})
	@method_decorator(login_required)
	def settings(self, request, action=None):
		context = {}
		if action == 'profile':
			context['is_profile']=True
			return render(request, 'handbook/accounts/settings/profile.html', context)
		
		elif action == 'edit_profile':
			context['is_profile']=True
			if request.method == 'POST':
				form = ProfileForm(request.POST, request.FILES, instance=request.user)
				if form.is_valid():
					form.save()
					messages.success(request, _("Profile successfully edit."))
					return HttpResponseRedirect(reverse('handbook:settings', kwargs={'action':'profile'}))
				else:
					messages.error(request, _("Form no valid."))
			else:
				form = ProfileForm(instance=request.user)
				context['form'] = form
			context['is_edit_profile']= True
			return render(request, 'handbook/accounts/settings/profile.html', context)
		
		else:
			messages.error(request, _("Action no found. Used action default."))

		return HttpResponseRedirect(reverse('handbook:index'))
