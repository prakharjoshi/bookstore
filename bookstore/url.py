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
	url(r'^bookshow$',views.bookshow,name='bookshow'),
	url(r'^maths$',views.maths,name='maths'),
	url(r'^science$',views.science,name='science'),
	url(r'^novels$',views.novel,name='novel'),
	url(r'^bookshow/(?P<book_id>\d+)/$',views.bookdetails, name='bookdetails'),
	url(r'^register/bookshow/$',views.bookshow,name = 'bookshow'),
	url(r'^addbook/$',views.addbook,name='addbook'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^invalid/$',views.invalid_login,name='invalid_login'),
	url(r'^company_details$',views.company_details,name='company_details'),
	url(r'^contact_us$',views.contact_us,name='contact_us'),
	url(r'^support$',views.support,name='support'),
	url(r'^privacy_policy$',views.private_policy,name='private_policy'),
	#url(r'^password_change/$',views.password_change,name='password_change'),
	#url(r'^password_change_done/$',views.password_change_done,name='password_change_done'),
	
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static('/bookshow/media', document_root=settings.MEDIA_ROOT)








