from django.db import models


class SiteInfo(models.Model):

    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    baseUrl = models.CharField(max_length=255, null=True)
    feedUrl = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255, null=True)
    lastModified = models.DateTimeField(null=True)
    etag = models.CharField(max_length=100, null=True)
    feedHash = models.CharField(max_length=32, null=True)
    imageLink = models.CharField(max_length=255, null=True)


class tags(models.Model):

    def __str__(self):
        return self.tag

    tag = models.CharField(max_length=255)
    siteId = models.ForeignKey(SiteInfo)
