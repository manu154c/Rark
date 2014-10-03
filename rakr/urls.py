from django.conf.urls import patterns, include, url
from django.contrib import admin

from feedReader.views import mainPage, testDataToDB, ajaxLoadFeeds
from accounts.views import loginview, auth_and_login, sign_up_in

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'rakr.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^reader/',include('feedReader.urls', namespace='reader')),
                       url(r'^$', mainPage),
                       url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^login/', loginview),
                       url(r'^auth/', auth_and_login),
                       url(r'^signup/', sign_up_in),
                       url(r'^test_data/', testDataToDB),
                       )
