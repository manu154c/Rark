from django.conf.urls import url

from tracker.views import trackOpenedPosts, trackNewTab

urlpatterns = [
                       #url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^track-opened-posts', trackOpenedPosts),
                       url(r'^redirect',trackNewTab),
                       ]
