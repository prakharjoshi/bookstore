from django.shortcuts import render_to_response
from django.template import RequestContext
from bookstore.models import book, author, publisher
from django.shortcuts import get_object_or_404, render



def bookshow(request):
	books = book.objects.all().order_by('name')
	context = {'books':books}
	return render_to_response('bookshow.html',context,context_instance = RequestContext(request))

def frontpage(request):
	return render_to_response('frontpage.html',context_instance = RequestContext(request))

