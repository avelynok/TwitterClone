from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser
import re
from notification.models import Notification
from django.views.generic import View

# Create your views here.
def add_tweet(request, id):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.get(id=id)
            users = MyUser.objects.all()
            tweet = Tweet.objects.create(
                tweet = data['tweet'],
                author = user
            )
            notify = re.findall(r'@(\w+)', data['tweet'])
            
            for user in notify: 
                Notification.objects.create(
                    receiver = MyUser.objects.get(displayname=user),
                    tweet = tweet,
                    )
            return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, 'addtweet.html', {'form': form})
    


class tweet_detail(View):
    def get(self, request, id):
        tweet = Tweet.objects.get(id=id)
        return render(request, 'tweet.html', {'tweet':tweet})