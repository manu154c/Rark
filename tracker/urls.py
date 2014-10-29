from django.conf.urls import patterns, url

from tracker.views import trackOpenedPosts, trackNewTab

urlpatterns = patterns('',
                       #url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^track-opened-posts', trackOpenedPosts),
                       url(r'^redirect',trackNewTab),
                       )
