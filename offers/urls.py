from django.conf.urls import patterns, url

from offers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name = 'account'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^createAccount/$', views.createAccount, name = 'createAccount'),
    url(r'^createEmployerAccount/$', views.createEmployerAccount, name = 'createEmployerAccount'),
    url(r'^createCandidateAccount/$', views.createCandidateAccount, name = 'createCandidateAccount'),
    url(r'^doCreateEmployerAccount/$', views.doCreateEmployerAccount, name = 'doCreateEmployerAccount'),
    url(r'^confirm/$', views.confirm, name = 'confirm'),
)