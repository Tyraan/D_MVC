from django.conf.urls import patterns, include, url
from django.contrib import admin
import procat

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd_mvc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^procat/',include('procat.urls')),
    url(r'^',include('procat.urls')),
)


