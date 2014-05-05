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
	url(r'^addbook/$',views.addbook,name='addbook'),
	url(r'^login/$',views.login,name='login'),
	#url(r'^auth/$','django_test.views.auth_view'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^invalid/$',views.invalid_login,name='invalid_login'),
	#url(r'^register/$',views.login, name = 'register'),
) 













