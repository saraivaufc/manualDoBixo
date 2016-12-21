from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.utils import timezone

from versatileimagefield.fields import VersatileImageField

class Item(models.Model):
	position = models.IntegerField(verbose_name=_("Position"), null= True, blank=True)
	topic = models.ForeignKey('Topic', verbose_name=_("Topic"))
	title = models.CharField(max_length=255, verbose_name=_("Title"), unique = True)
	slug = models.SlugField(_('slug'), max_length=60, blank=True, unique=True)
	creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)

	description = models.TextField(verbose_name=_("Description"))
	image = VersatileImageField(verbose_name=_("Image"),upload_to = 'documents/%Y/%m/%d', default=None)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Item, self).save(*args, **kwargs)

	def set_topic(self, topic):
		self.topic = topic

	def get_position(self):
		return self.position

	def get_topic(self):
		return self.topic

	def get_title(self):
		return self.title

	def get_slug(self):
		return self.slug

	def get_description(self):
		return self.description

	def get_image(self):
		return self.image

	def get_creation(self):
		return self.creation

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['position']
		verbose_name = "Item"
		verbose_name_plural = "Items"
