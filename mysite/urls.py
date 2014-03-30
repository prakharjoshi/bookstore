from django.conf.urls import patterns, include, url
from bookstore import views
from django.views.generic import TemplateView
#from .. import bookstore.views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/', views.frontpage),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^bookshow/',views.bookshow),
)
