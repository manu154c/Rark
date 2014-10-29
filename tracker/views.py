from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import logging


from tracker.models import Tracker

logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/login/')
def trackOpenedPosts(request):
    try:
        postId = request.GET['post_id']
        user = request.user
        record = Tracker(userId=user, postId=postId)
        record.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def trackNewTab(request):
    # to do check the record alreadr exists or not if yes  SiteInfo.objects.filter(id=siteId)
    postId = request.GET['p_id']
    url = request.GET['url']
    user = request.user
    try:
        record = Tracker.objects.filter(userId=user, postId=postId)
        record = record[0]
        logger.info('Existing entry')
    except:
        record = Tracker()
        logger.info('New entry')
    try:
        record.postId = postId
        record.userId = user
        record.openInNewTab = True
        logger.info('Assigned values')
        record.save()
        logger.info('saved values')
        return render_to_response('goto.html', {'url': url})
    except:
        return render_to_response('goto.html', {'url': url})
