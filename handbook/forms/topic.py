from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from handbook.models import *

class TopicForm(ModelForm):
	class Meta:
		model= Topic
		exclude  = ['position','slug', 'creation']
		widgets = {
			'title': TextInput(attrs={'required': 'required'}),
		}