from django.shortcuts import *
from django.template import RequestContext
from django import forms
from bookstore.models import book, author, publisher, signup
from django.shortcuts import get_object_or_404, render
from bookstore.forms import SignUpForm


def home(request):
	return render_to_response('bookstore/frontpage.html/',context_instance=RequestContext(request))

def bookshow(request):
	books = book.objects.all().order_by('name')
	#context = {'books':books}
	return render(request,'bookstore/bookshow.html/',{'books':books})
	form = SignUpForm()
#def frontpage(request):
	#SSreturn render_to_response('frontpage.html',context_instance = RequestContext(request))

def bookdetails(request , book_id):
	#authors = book.objects.get(author)
	authors = get_object_or_404(author , pk=book_id)
	publishers = get_object_or_404(publisher, pk=book_id)
	#context = {'authors':authors, 'publishers':publishers}
	return render(request,'bookstore/bookdetail.html/',{'authors':authors,'publishers':publishers})


def contact(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		username = request.get=['name']
		password = request.get=['password']

		if form.is_valid():
			#username = form.cleaned_data['username']
			#password = form.cleaned_data['password']
		
			form.save()
			message = "Your account has been successfully created"
		else:
			message = "something went wrong"

		return render_to_response('bookstore/signup.html',{'form':form},context_instance = RequestContext(request))

	else:
		return render_to_response('bookstore/signup.html',{'form':SignUpForm()},context_instance = RequestContext(request))










