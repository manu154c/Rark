from django.conf.urls import patterns, url

from feedReader.views import testDataToDB, ajaxLoadFeeds, getExpandedPost

urlpatterns = patterns('',
                       url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^get-expanded-post', getExpandedPost),
                       url(r'^test_data/', testDataToDB),
                       )
