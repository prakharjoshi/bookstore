from django.conf.urls import patterns, url
from bookstore import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(' ',
	url(r'^$',views.home, name = 'home'),
	#url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^register/$', views.register,name='register'),
	url(r'^search/$',views.search, name = 'search'),
	url(r'^about/$',views.about,name='about'),
	url(r'^bookshow/$',views.bookshow,name='bookshow'),
	url(r'^maths$',views.maths,name='maths'),
	url(r'^science$',views.science,name='science'),
	url(r'^novel$',views.novel,name='novel'),
	url(r'^bookshow/(?P<book_id>\d+)/$',views.bookdetails, name='bookdetails'),
	url(r'^register/bookshow/$',views.bookshow,name = 'bookshow'),
	url(r'^addbook/$',views.addbook,name='addbook'),
	url(r'^accounts/login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^invalid/$',views.invalid_login,name='invalid_login'),
	#url(r'^password_change/$',views.password_change,name='password_change'),
	#url(r'^password_change_done/$',views.password_change_done,name='password_change_done'),
	
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)












