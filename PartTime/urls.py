from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^offers/', include('offers.urls', namespace="offers")),
    url(r'^admin/', include(admin.site.urls)),
)
