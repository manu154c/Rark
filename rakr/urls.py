from django.conf.urls import patterns, include, url
from django.contrib import admin

from feedReader.views import mainPage

urlpatterns = patterns('',
                       #url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', mainPage),
                       url(r'^reader/', include('feedReader.urls', namespace='reader')),
                       url(r'^accounts/', include('accounts.urls', namespace='accounts')),
                       url(r'^tracker/', include('tracker.urls', namespace='tracker')),
                       url(r'^predictor/', include('predictor.urls', namespace='predictor')),
                       )
