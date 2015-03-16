from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from newspaper.forms import PartialLectorForm
try:
	from hashlib import md5
except:
	from md5 import new as md5

def login(request):
	if request.user.is_authenticated():
		print "entrou porra"
		return HttpResponseRedirect("/newspaper/")

	if request.method == "POST":

		try:
			username = request.POST['username']
			password = request.POST['password']
		except:
			print "bsta"
			pass

		user = authenticate(username=username, password=password)
		if user:
			login_user(request, user)
			return login(request)
		else:
			print "sdsd"

	else:
		pass
	return HttpResponseRedirect("/newspaper/")

def logout(request):
	logout_sys(request)
	return login(request)

def signup(request):
	request.POST = request.POST.copy()
	request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
	form = PartialLectorForm(request.POST)
	if form.is_valid():
		try:
			form.save()
		except:
			print "Falha ao adicionar Lector"

	return HttpResponseRedirect("/newspaper/")
