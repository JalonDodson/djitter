# Generated by Django 3.1.7 on 2021-03-01 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_tweets', '0003_auto_20210301_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 17, 51, 38, 488377, tzinfo=utc)),
        ),
    ]
