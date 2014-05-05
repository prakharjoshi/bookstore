from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contib import auth
from django.core.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(reqquest))
	return render_to_response('sucessfully_login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username = username, password = password)
	if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('bookstore/sucessful_login.html/')
	else:
		return HttpResponseRedirect('bookstore/invalid_login.html/')


def logged_in(request):
	return render_to_response('bookstore/sucessful_login.html',{'first_name': request.user.username})

def invalid_login(request):
	return render_to_response('bookstore/invalid_login.html/')

def logout(request):
	auth.logout(request)
	return render_to_response('bookstore/logout.html/')
