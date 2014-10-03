# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=255)),
                ('baseUrl', models.CharField(null=True, max_length=255)),
                ('feedUrl', models.CharField(max_length=255)),
                ('subTitle', models.CharField(null=True, max_length=255)),
                ('lastModified', models.DateTimeField(null=True)),
                ('etag', models.CharField(null=True, max_length=100)),
                ('feedHash', models.CharField(null=True, max_length=32)),
                ('imageLink', models.CharField(null=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(max_length=255)),
                ('siteId', models.ForeignKey(to='feedReader.SiteInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
