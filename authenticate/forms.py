from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	telefono = forms.CharField(max_length=20, label="telefono", help_text='inserte código de area.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'password1', 'password2',)