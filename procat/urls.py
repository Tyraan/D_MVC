from django.conf.urls import patterns, url

from procat import views


urlpatterns = patterns('',
    url(r'^$',          views.index,  name='index'),
    url(r'^showCat',    views.showCat, name='showCat'),
    url(r'^addCat',     views.addCat, name='addCat'),
    url(r'^delCat',     views.delCat, name='addCat'),
    url(r'^showPro',    views.showPro,name='showPro'),
    url(r'^addPro',     views.addPro, name = 'addPro'),
    url(r'delPro',      views.delPro, name = 'delPro'),
  )