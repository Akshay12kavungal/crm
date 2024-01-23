from django import forms

from Student.models import StudentDetail

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomerFilterForm(forms.ModelForm):

	class Meta:
		model = StudentDetail
		fields = ['status']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

