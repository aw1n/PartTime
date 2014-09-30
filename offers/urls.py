from django.conf.urls import patterns, url

from offers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name = 'account'),
)