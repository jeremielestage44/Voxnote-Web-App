
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm



# fonction vue pour que l'utilisateur se crée un compte avec le form de création de compte
def creerCompte(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('voxnote-login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/creerCompte.html', {'form': form, 'title':'Créer un compte'})




# fonction vue pour que l'utilisateur se connecte a son compte 
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request,user)
			return redirect('voxnote-accueil')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'Se connecter'})
