from django.conf.urls import patterns, include, url
from bookstore import views
#from visitors import views
#from bookstore import url
#from django.views.generic import TemplateView
#from .. import bookstore.views
from django.contrib import admin
from django.contrib import auth
#from django.conf import settings
#from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'','bookstore.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('bookstore.url')),
    #url(r'^registration/',include('visitors.url')),
    #url(r'^contact/$', 'bookstore.views.url'),
   	#contact(r'^accounts/login/$', 'django_test.views.login'),
   	#url(r'^accounts/auth/$' ,  'django_test.views.auth_view')
	#url(r'^accounts/logout/$', 'django_test.views.logout'),
	#url(r'^accounts/logggedin/$', 'django_test.views.logggedin'),
	#url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),

)