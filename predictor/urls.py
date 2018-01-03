from django.conf.urls import url

from predictor.views import preparePosts, calculatePref

urlpatterns = [
                       #url(r'^load-more-short-feeds', ajaxLoadFeeds),
                       url(r'^prepare-posts', preparePosts),
                       url(r'^calculate-pref', calculatePref),
                       ]
