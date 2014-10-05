import hashlib

from django.http import Http404

from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId


class Mongo():

    '''
    This class contain all the functions to access MONGODB
    '''

    def __init__(self):
        '''
        Use the connection variable in the settings to use MONGODB
        '''
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.ireadr

    def insertFeeds(self, feeds, siteId):
        '''
        insert the feeds in to database collection:feeds
        '''
        hashFeed = self.md5Feeds(feeds)
        if(self.isFeedExists(hashFeed=hashFeed)):
            return
        if(self.isFeedExists(id=feeds.id)):        # for updating modified posts
            self.db.feeds.update({"feed.title": feeds.title}, {"$set": {"feed": feeds, "hashFeed": hashFeed}})
        else:
            self.db.feeds.insert({"feed": feeds, "siteId": siteId, "hashFeed": hashFeed})

    def isFeedExists(self, hashFeed=None, id=None):
        if id is None:
            if(self.db.feeds.find({"hashFeed": hashFeed}).count()):
                return True
            return False
        else:
            if(self.db.feeds.find({"feed.id": id}).count()):
                return True
            return False

    def selectFeedById(self, id):
        '''
        Select a single feed by __dirname
        '''
        try:
            feed = self.db.feeds.find_one({"_id": ObjectId(id)})
            return feed
        except:
            raise Http404

    def selectFeeds(self, dateOfLastItem=None, limit=10):
        '''
        select feeds sorted in reverse chronological order.
        select 'limit' items published before dateOfLastItem
        '''
        if dateOfLastItem is None:
            allFeeds = self.db.feeds.find().sort([("feed.published_parsed", -1)]).limit(limit)
        else:
            allFeeds = self.db.feeds.find({"feed.published_parsed": {"$lt": dateOfLastItem}}).sort(
                [("feed.published_parsed", -1)]).limit(limit)
        return allFeeds

    def md5Feeds(self, feed):
        '''
        find md5 of feed
        '''
        md5 = hashlib.md5(str(feed).encode('utf-8'))
        return md5.hexdigest()
