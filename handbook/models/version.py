from django.db import models
from django.utils.translation import ugettext as _

class Version(models.Model):
	name = models.CharField(max_length=255, verbose_name=_("Name"), unique = True) 
	version = models.IntegerField(verbose_name=_("Version"), default=1)