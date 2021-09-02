from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Document
from django.contrib import messages

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'email']
        labels = {'email':'Email'}


class DocumentForm(forms.ModelForm):
	""" Form for Document model"""
	class Meta:
		model = Document
		fields = ['title','pdf']



