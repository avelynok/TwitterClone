from django.db import models
from twitteruser.models import MyUser
from django.utils import timezone

class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.tweet
