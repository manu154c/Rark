from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from feedReader.mongoFunctions import Mongo
import logging


from tracker.models import Tracker

logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/login/')
def trackOpenedPosts(request):
    mongo = Mongo()
    try:
        postId = request.GET['post_id']
        user = request.user
        post = mongo.selectFeedById(postId)
        userObj = mongo.selectUser(user.id)
        postVals = post['depValues']
        userVals = userObj['depValues']
        for entry in userVals:
            userVals[entry] = 0.16*postVals[entry]+0.84*userVals[entry]
        record = Tracker(userId=user, postId=postId)
        record.save()
        mongo.updateUserValues(user.id, userVals)
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def trackNewTab(request):
    
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
