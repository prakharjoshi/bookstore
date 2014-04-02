from django.conf.urls import patterns, include, url
#from bookstore import views
#from bookstore import url
#from django.views.generic import TemplateView
#from .. import bookstore.views
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookstore/',include('bookstore.url')),
)
