from django.conf.urls import patterns, url
from bookstore import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(' ',
	url(r'^$',views.home, name = 'home'),
	url(r'^sign/$', views.signup,name='sign'),
	url(r'^search/$',views.search, name = 'search'),
	url(r'^bookshow/$',views.bookshow,name='bookshow'),
	url(r'^bookshow/(?P<book_id>\d+)/$',views.bookdetails, name='bookdetails'),
	url(r'^contact/$',views.contact, name = 'contact')

) 


