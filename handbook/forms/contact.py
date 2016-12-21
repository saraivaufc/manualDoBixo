from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from handbook.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model= Contact