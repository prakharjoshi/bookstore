#from django.db import models
#from django.forms import ModelForm
from django import forms
#from forms import SignUp
from bookstore.models import User
from django.contrib.auth.models import User 

TITLE_CHOICES = (
		('MR' , 'Mr'),
		('MRS', 'Mrs'),
		('MS' , 'Ms'),
)

"""class Author(models.Model):
	name = models.CharField(max_length=100)
	title = models.Charfield(max_length=3 , choices=TITLE_CHOICES)
	#birth_date = models.DateField(blank=True, null=True)

	def __unicode__ (self):
		return self.name

class Book(models.Model):
	name = models.Charfield(max_length=100)
	authors = models.ManyToManyFields(Author)"""

"""class AuthForm(ModelForm):
	class Meta:
		models = author
		fields = ['name','title','birth_date']

class BookForm(ModelForm):
	class Meta:
		model = book
		fields = ['name','authors']"""

"""class SignUpForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=50)"""




"""class Meta:
		model = signup
		fields = ['username','password']"""


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class meta:
		model = User