from django.conf.urls import url

from feedReader.views import testDataToDB, ajaxLoadFeeds, getExpandedPost

urlpatterns = [
                       url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^get-expanded-post', getExpandedPost),
                       url(r'^test_data/', testDataToDB),
                       ]
