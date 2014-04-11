from django.conf.urls import patterns, url
from bookstore import views

urlpatterns = patterns(' ',
	url(r'^$',views.contact, name = 'bookshow'),
	url(r'^(?P<book_id>\d+)/$',views.bookdetails, name='bookdetails')
)
