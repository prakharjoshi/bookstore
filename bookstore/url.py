from django.conf.urls import patterns, url
from bookstore import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(' ',
	url(r'^$',views.home, name = 'home'),
	url(r'^register/$', views.register,name='register'),
	url(r'^search/$',views.search, name = 'search'),
	url(r'^about/$',views.about,name='about'),
	url(r'^bookshow/$',views.bookshow,name='bookshow'),
	url(r'^bookshow/(?P<book_id>\d+)/$',views.bookdetails, name='bookdetails'),
	url(r'^register/bookshow/$',views.bookshow,name = 'bookshow'),
	#url(r'^register/$',views.login, name = 'register'),
) 













