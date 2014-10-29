from django.db import models


class DepWords(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255, null=True)
    value = models.FloatField()
    samples = models.IntegerField()
    category = models.CharField(max_length=255, null=False)

    class Meta:
        unique_together = ('word', 'category')
