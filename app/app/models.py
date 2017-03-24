from django.db import models
import datetime
from django.contrib.auth.models import User

class TweetInfo(models.Model):
 	user = models.ForeignKey(User)
	tweet_id=models.CharField(max_length=1000, blank=False)
	tweet_text=models.CharField(max_length=1000, blank=False)
	tweet_agression=models.CharField(max_length=3, blank=False)
	def __unicode__(self):
		return self.tweet_id