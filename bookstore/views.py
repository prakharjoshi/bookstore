from django.shortcuts import *
from django.template import RequestContext
from django.core.mail import send_mail
from bookstore.models import book, author, publisher
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset,password_change,password_change_done,password_reset_done,password_reset_confirm
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.views import password_reset




def home(request):
	return render_to_response('bookstore/frontpage.html/',context_instance=RequestContext(request))

def contact_us(request):
	return render_to_response('bookstore/contact_us.html/',context_instance=RequestContext(request))

def company_details(request):
	return render_to_response('bookstore/company_details.html/',context_instance=RequestContext(request))

def private_policy(request):
	return render_to_response('bookstore/privacy_policy.html/',context_instance=RequestContext(request))

def support(request):
	return render_to_response('bookstore/support.html/',context_instance=RequestContext(request))
	
@login_required(login_url='/login/')
def bookshow(request):
	books = book.objects.all().order_by('name')
	return render(request,'bookstore/bookshow.html/',{'books':books})
	

def maths(request):
	b = book.objects.filter(category='maths')
	return render(request,'bookstore/bookshow_maths.html/',{'b':b})

def science(request):
	c = book.objects.filter(category='science')
	return render(request,'bookstore/bookshow_science.html/',{'c':c})

def novel(request):
	a = book.objects.filter(category='novel')
	return render(request,'bookstore/bookshow_novel.html/',{'a':a})




@login_required(login_url='/login/')
def bookdetails(request , book_id):
	authors = get_object_or_404(author , pk=book_id)
	publishers = get_object_or_404(publisher, pk=book_id)
	return render(request,'bookstore/bookdetail.html/',{'authors':authors,'publishers':publishers})



def search_form(request):
	return render(request,'bookstore/search_form.html')

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = book.objects.filter(name = q)
			return render(request,'bookstore/search.html',{'books':books,'query':q})
	else:		
		return render(request,'bookstore/search_form.html',{'error':error})



def register(request):
	error = []
	if request.method == "POST":
		user_form = User.objects.create_user( username = request.POST['username'],password = request.POST['password'],
		 					email = request.POST['email'],first_name = request.POST['first_name'],
		 					last_name = request.POST['last_name'])

		
		user_form.save()
		return HttpResponseRedirect('/')
			
	else:
		error.append("invalid information")

		

	return render(request,'bookstore/register.html',{'error':error})


		
	
@login_required(login_url='/login/')
def addbook(request):
	error = []
	if request.method == "POST":
		b = book()
		b.name = request.POST['bookname']
		b.category = request.POST['category']
		a = author()
		a.first_name = request.POST['author']
		a.save()
		b.author = a
		p = publisher()
		p.name = request.POST['publisher']
		p.save()
		b.publisher = p
		b.docfile = request.FILES['file']
		b.save()

		
        
		return HttpResponseRedirect('/bookshow')
	else:
		error.append('all fields are required')
	
	return render(request,'bookstore/addbook.html',{'error':error})




def login(request):
	error = []
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		if user is not None:
				auth.login(request,user)
				return HttpResponseRedirect('/bookshow')
		else:
			return HttpResponseRedirect('/invalid/')
	else:
		error.append("invalid information")
	return render(request,'bookstore/login.html',{'error':error})




def invalid_login(request):
	return render_to_response('bookstore/invalid_login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')








