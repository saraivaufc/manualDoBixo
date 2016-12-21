from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.utils import timezone 
from .item import Item

class Topic(models.Model):
	position = models.IntegerField(verbose_name=_("Position"), null= True, blank=True)
	title = models.CharField(max_length=255, verbose_name=_("Title"), unique = True)
	slug = models.SlugField(_('slug'), max_length=60, blank=True, unique=True)
	creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Topic, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title


	class Meta:
		ordering = ['position']
		verbose_name = "Topic"
		verbose_name_plural = "Topics"

	def get_position(self):
		return self.position

	def get_title(self):
		return self.title

	def get_slug(self):
		return self.slug

	def get_items(self):
		return Item.objects.filter(topic = self.id)

	def items(self):
		from handbook.api.serializers import ItemSerializerPk
		return ItemSerializerPk(self.get_items(), many=True).data
	def get_creation(self):
		return self.creation


