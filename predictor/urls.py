from django.conf.urls import patterns, url

from predictor.views import preparePosts, calculatePref

urlpatterns = patterns('',
                       #url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^prepare-posts', preparePosts),
                       url(r'^calculate-pref', calculatePref),
                       )
