from django.conf.urls import patterns, url

from feedReader.views import mainPage, testDataToDB, ajaxLoadFeeds

urlpatterns = patterns('',
                       url(r'^$', mainPage),
                       url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^login/', loginview),
                       url(r'^auth/', auth_and_login),
                       url(r'^signup/',sign_up_in),
                       url(r'^test_data/', testDataToDB),
                       )
