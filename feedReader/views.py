from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from feedReader.ParsingFunctions import ParsingFuncs
import time
import datetime
from feedReader.models import SiteInfo
from django.http import HttpResponse
import json
import iso8601


@login_required(login_url='/accounts/login/')
def mainPage(request):
    parseFn = ParsingFuncs()
    # need to add this as a cron job
    #parseFn.fetchFeeds()
    allFeeds = parseFn.allFeeds()
    feedsToDisplay = []
    for i in allFeeds:
        temp = {}
        temp['id'] = i['_id']
        temp['title'] = i['feed']['title']
        temp['siteTitle'] = parseFn.getSiteTitle(i['siteId'])
        temp['summary'] = parseFn.getSummary(i['feed']['summary'])
        temp['link'] = i['feed']['link']
        temp['image'] = i['feed']['image_link']
        feedsToDisplay.append(temp)
    dateOfLastItem = i['feed']['published_parsed'].isoformat()
    return render_to_response('main.html', {'feeds': feedsToDisplay, 'lastDate': dateOfLastItem})


def ajaxLoadFeeds(request):
    parseFn = ParsingFuncs()
    try:
        dateOfLastItem = request.GET["last_date"]
        dateOfLastItem = iso8601.parse_date(dateOfLastItem)
    except:
        dateOfLastItem = None

    feedsToDisplay = []
    allFeeds = parseFn.allFeeds(lastDate=dateOfLastItem)
    for i in allFeeds:
        temp = {}
        temp['id'] = str(i['_id'])
        temp['title'] = i['feed']['title']
        temp['siteTitle'] = parseFn.getSiteTitle(i['siteId'])
        temp['summary'] = parseFn.getSummary(i['feed']['summary'])
        temp['link'] = i['feed']['link']
        temp['image'] = i['feed']['image_link']
        temp['date'] = i['feed']['published_parsed'].isoformat()
        feedsToDisplay.append(temp)
    feedsJSON = json.dumps(feedsToDisplay)
    return HttpResponse(feedsJSON, content_type="application/json")


def getExpandedPost(request):
    parseFn = ParsingFuncs()
    id = request.GET['post_id']
    feed = parseFn.selectFeedById(id)
    temp = {}
    temp['id'] = str(feed['_id'])
    temp['title'] = feed['feed']['title']
    temp['link'] = feed['feed']['link']
    temp['siteTitle'] = parseFn.getSiteTitle(feed['siteId'])
    temp['post'] = parseFn.getFullPost(feed['feed']['summary_detail']['value'])
    temp['image'] = feed['feed']['image_link']
    temp['date'] = feed['feed']['published_parsed'].isoformat()
    feedJson = json.dumps(temp)
    return HttpResponse(feedJson, content_type="application/json")


def tryFullPost(request):
    '''
    try to load the full post inside the application itself
    (not used now- can be used- its working)
    '''
    parseFn = ParsingFuncs()
    link = request.POST['link']
    summary = request.POST['summary']
    post = parseFn.getFullPostURLOpen(link, summary)
    return HttpResponse(post)


def testDataToDB(request):
    '''
    function defined to add sample data to db. Need to be deleted.
    '''
    structTime = time.localtime()
    dt = datetime.datetime(*structTime[:6])
    si = SiteInfo()
    si.title = "LifeHacker"
    si.baseUrl = "http://lifehacker.com"
    si.feedUrl = "http://lifehacker.com/rss"
    si.lastModified = dt
    si.save()

    sj = SiteInfo()
    sj.baseUrl = "http://techcrunch.com"
    sj.feedUrl = "http://techcrunch.com/feed"
    sj.title = "TechCrunch"
    sj.lastModified = dt
    sj.save()

    return HttpResponse("True")
