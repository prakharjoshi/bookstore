from django.shortcuts import render_to_response
from django.template import RequestContext
from bookstore.models import book, author, publisher
from django.shortcuts import get_object_or_404, render



def bookshow(request):
	books = book.objects.all().order_by('name')
	#context = {'books':books}
	return render(request,'bookstore/bookshow.html/',{'books':books})

#def frontpage(request):
	#SSreturn render_to_response('frontpage.html',context_instance = RequestContext(request))

def bookdetails(request , book_id):
	#authors = book.objects.get(author)
	authors = get_object_or_404(author , pk=book_id)
	#context = {'authors':authors, 'publishers':publishers}
	return render(request,'bookstore/bookdetail.html/',{'authors':authors})

