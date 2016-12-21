from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from handbook.models import *

import hashlib
from handbook.widgets import AdvancedFileInput

class ItemForm(ModelForm):
	class Meta:
		model= Item
		fields = ("topic","title", "description", "image")
		widgets = {
			'image': AdvancedFileInput(attrs={}),
		}
		
	def clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image and image.name.find('manualdocalouro_') == -1:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "manualdocalouro_" + "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
		