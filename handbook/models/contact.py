from django.db import models
from django.utils.translation import ugettext as _


class Contact(models.Model):
	name = models.CharField(max_length=255, verbose_name=_("Name"))
	email = models.EmailField(verbose_name=_("Email"))
	message = models.TextField(verbose_name=_("Message"))

	def get_name(self):
		return self.name

	def get_email(self):
		return self.email

	def get_message(self):
		return self.message	

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-name']
		verbose_name = _("Name")
		verbose_name_plural = _("Names")