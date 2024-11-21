from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):# Form que l'utilisateur doit remplir pour se créer un compte
	class Meta:
		model = User
		fields = ['username','password1', 'password2']