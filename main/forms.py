from django import forms
import datetime

from .models import (
	User,
	Profile
	)

class DateInput(forms.DateInput):
	input_type = 'date'

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['username'].widget.attrs['disabled'] = True

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'location', 'birth_date')
		widgets = {
            'birth_date': DateInput(),
        }
