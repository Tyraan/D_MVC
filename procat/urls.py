from django.conf.urls import patterns, url
from procat import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^showCat',views.showCat,name='showCat'),
    url(r'^addCat',views.addCat,name='addCat'),
    url(r'^delCat',views.delCat,name='addCat'),
                      )