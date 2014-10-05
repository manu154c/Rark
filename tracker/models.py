from django.db import models

from django.contrib.auth.models import User


class Tracker(models.Model):

    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User)
    postId = models.CharField(max_length=24, null=False)
    openInNewTab = models.BooleanField(default=False)
    visitedExternalLinks = models.BooleanField(default=False)
