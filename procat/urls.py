from django.conf.urls import patterns, url
from procat import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^showCat',views.showCat,name='showCat'),
                      )