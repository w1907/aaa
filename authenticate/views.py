from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from authenticate.forms import SignUpForm

def signIn(request):
	data = {}
	template_name = 'login.html'
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				messages.warning(request, "Correo o contraseña invalidos")
		else:
			messages.warning(request, "Correo o contraseña invalidos")
	return render(request, template_name, data)

def signOut(request):
	data = {}
	template_name = 'logout.html'
	logout(request)
	return render(request, template_name, data)

def signUp(request):
	template_name = 'registro.html'
	if request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.telefono = form.cleaned_data.get('telefono')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = SignUpForm()
	return render(request, template_name, {'form': form})