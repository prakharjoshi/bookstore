from django.shortcuts import *
from django.template import RequestContext
from django.core.mail import send_mail
#from django import forms
from bookstore.models import book, author, publisher,signup,sign,User
#from django.shortcuts import get_object_or_404, render
#from bookstore.forms import SignUpForm
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.decorators import login_required,user_passes_test


def home(request):
	return render_to_response('bookstore/frontpage.html/',context_instance=RequestContext(request))

def bookshow(request):
	books = book.objects.all().order_by('name')
	#context = {'books':books}
	return render(request,'bookstore/bookshow.html/',{'books':books})
	#form = SignUpForm()
#def frontpage(request):
	#SSreturn render_to_response('frontpage.html',context_instance = RequestContext(request))

def bookdetails(request , book_id):
	#authors = book.objects.get(author)
	authors = get_object_or_404(author , pk=book_id)
	publishers = get_object_or_404(publisher, pk=book_id)
	#context = {'authors':authors, 'publishers':publishers}
	return render(request,'bookstore/bookdetail.html/',{'authors':authors,'publishers':publishers})

"""def sign(request):
	if request.POST:
		username = request.POST['username']
		user = signup.objects.create(username = username)
		return render(request,'bookstore/logged_in.html',{'username':user})
	return render(request,'bookstore/login.html')"""



def signin(request):
	if request.POST:
		username = request.POST['username']
		user = sign.objects.create(username = username)
		return render(request,'bookstore/logged_in.html',{'username':user})
	return render(request,'bookstore/login.html')










	
	





	#username = request.POST['username']
    	#user = signup.objects.create(username=username)
    	#return render(request,'bookstore/signup.html',{'username': username})
		
		#return HttpResponseRedirect(reverse(('bookstore:bookshow'),args = (username.id)))


	
	

	#return render(request,'bookstore/signup.html')


"""def contact(request):
	if request.method == 'POST':
		username = request.POST.get('username',False)
		password = request.POST.get('password',False)
		form = SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			message = "your account has been successfully created"
		else:
			message = "something went wrong"
			return render(request,'bookstore/signup.html',{'success':message})
	else:
		return render(request,'bookstore/signup.html',{'form':SignUpForm()})

	#username = signup.objects.get(username=username)
	#password = signup.objects.get(password=password)
	if request.method == 'POST':
		username = request.GET=['name']
		password = request.GET=['password']
		form = SignUpForm(data=request.POST)

		

		if form.is_valid():	
			form.save()
			message = "Your account has been successfully created"
		else:
			message = "something went wrong"

		return render_to_response('bookstore/signup.html',{'success':message},context_instance = RequestContext(request))

	else:
		return render_to_response('bookstore/signup.html',{'form':SignUpForm()},context_instance = RequestContext(request))"""
		
		
		
			











#username = signup.objects.get(username=username)
			#password = signup.objects.get(password=password)
			#username = form.cleaned_data['username']
			#password = form.cleaned_data['password']"""

"""def email_check(user):
	return '@example.com' in user.email 

@user_passes_test(email_check,login_url'/login/')
@login_required(login_url = 'account/login')
def my_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password=password)
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	if user is not None:
		if user.is_active:
			login(request,user)
			return render(request,'bookstore/bookshow.html')
		else:
			return render(request,'bookstore/error.html')
	else:
		return render(request,'bookstore/invalid_login.html')

def logout_view(request):
	logout(request)
	return render(request,'bookstore/logout.html')"""




"""def contact(request):
	errors = []
	if request.method == "POST":
		if not request.POST.get('username',''):
			errors.append('enter username')
		if not errors:
			request.POST['username']
			return HttpResponseRedirect('sign/thanks')

	return render(request,'bookstore/signup.html',{'username':request.POST.get('username',''),'errors':errors})"""

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

"""def contact(request):
	errors = []
	if request.method == "POST":
		if not request.POST.get('subject',''):
			errors.append('enter a subject')
		if not request.POST.get('message',''):
			errors.append('enter message')
		if request.POST.get('email') & '@' not in request.POST['email']:
			errors.append('please enter a valid email address')
		if not errors:
			send_email(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email', 'noreply@example.com'),
				['site_owner@example.com'],
				)
			return HttpResponseRedirect('/contact/thanks')
	return render(request,'bookstore/contact_form.html',{'errors':errors,
					'subject':request.POST.get('subject',''),
					'message':request.POST.get('message',''),
					'email':request.POST.get('email','')})"""


def register(request):
	#registered = False
	error = []
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		username.save()
		password.save()

		User.objects.create(username = username, password = password)
		#registered = True
		
	else:
		error.append('All fields are required') 

	return render(request,'bookstore/signup.html',{'error':error})




