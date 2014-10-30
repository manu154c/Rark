import hashlib

from django.http import Http404

from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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
        depValues = {
            "automobile": 0.0,
            "bussiness": 0.0,
            "fashion": 0.0,
            "food": 0.0,
            "health": 0.0,
            "history": 0.0,
            "movie": 0.0,
            "music": 0.0,
            "real-estate": 0.0,
            "science": 0.0,
            "sports": 0.0,
            "technology": 0.0,
            "travel": 0.0
        }
        hashFeed = self.md5Feeds(feeds)
        if(self.isFeedExists(hashFeed=hashFeed)):
            return
        # for updating modified posts
        if(self.isFeedExists(id=feeds.id)):
            self.db.feeds.update(
                {"feed.title": feeds.title}, {"$set": {"feed": feeds, "hashFeed": hashFeed}})
        else:
            self.db.feeds.insert(
                {"feed": feeds, "siteId": siteId, "hashFeed": hashFeed, "depValues": depValues, "processed": 0})

    def isFeedExists(self, hashFeed=None, id=None):
        if id is None:
            if(self.db.feeds.find({"hashFeed": hashFeed}).count()):
                return True
            return False
        else:
            if(self.db.feeds.find({"_id": id}).count()):
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

    def selectFeeds(self, user_id, dateOfLastItem=None, limit=20):
        '''
        select feeds sorted in reverse chronological order.
        select 'limit' items published before dateOfLastItem
        '''

        if dateOfLastItem is None:
            allFeeds = self.db.feeds.find({"processed": 1, "pref."+str(user_id):{"$exists":1}}).sort(
                [("feed.published_parsed", -1)]).limit(limit)
        else:
            allFeeds = self.db.feeds.find({"processed": 1, "pref."+str(user_id):{"$exists":1}, "feed.published_parsed": {"$lt": dateOfLastItem}}).sort(
                [("feed.published_parsed", -1)]).limit(limit)
        return allFeeds

    def md5Feeds(self, feed):
        '''
        find md5 of feed
        '''
        md5 = hashlib.md5(str(feed).encode('utf-8'))
        return md5.hexdigest()

    def selectUnProcessedFeeds(self):
        '''
        select all feeds which are not classified. ie. processed=0
        '''

        allFeeds = self.db.feeds.find({"processed": 0})
        return allFeeds

    def selectProcessedFeeds(self, user_id):
        '''
        select all feeds which are already classified. ie. processed=1
        '''

        allFeeds = self.db.feeds.find({"processed": 1, "pref.user_id": {'$ne': user_id}})
        return allFeeds


    def updateDepValues(self, id, depValues):
        if(self.isFeedExists(id=id)):
            # logger.info(id)
            # logger.info(depValues)
            self.db.feeds.update(
                {"_id": id}, {"$set": {"depValues": depValues, "processed": 1}})

    def addTestUser(self):
        '''
        Useless function can be removed
        '''
        depValues = {
            "automobile": 0.5,
            "bussiness": 0.5,
            "fashion": 0.0,
            "food": 0.0,
            "health": 0.5,
            "history": 0.5,
            "movie": 0.5,
            "music": 0.5,
            "real-estate": 0.0,
            "science": 0.5,
            "sports": 0.0,
            "technology": 0.5,
            "travel": 0.5
        }
        self.db.user.insert({"user_id": 1, "depValues": depValues})

    def selectUser(self, user_id):
        user = self.db.user.find_one({"user_id" : user_id})
        return user

    def updateUserPref(self, id, pref):
        '''
        sets user's preference in feed collection
        '''
        self.db.feeds.update({"_id": id},{"$set":{"pref": pref}})

    def updateUserValues(self, id, depVals):
        '''
        Sets user's pref in user collection
        '''
        self.db.user.update({"user_id": id},{"$set":{"depValues":depVals}})