from django import forms
from .models import *

class VESSEL_Form(forms.ModelForm):

	description = forms.CharField(widget=forms.Textarea,required=False,initial='This field is optional')

	class Meta:
		model = VESSEL
		fields = ('project_number', 'name', 'description', 'image')