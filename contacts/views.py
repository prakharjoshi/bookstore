from django.shortcuts import *
from django.template import RequestContext


def contact(request):
	if request.method == "POST":
		request.POST=['name']
		request.POST=['message']
		message = "thank you for your feedback"


		return render_to_response('contact/contact.html',{success:'message'},context_instance = RequestContext(request))

	else:
		return render_to_response('contact/contact.html',{},context_instance = RequestContext(request))


