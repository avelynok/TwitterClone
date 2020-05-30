from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import MyUser
from twitteruser.forms import SignupForm
from django.contrib.auth import login, authenticate
from tweet.models import Tweet

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password1'],
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'SignupForm.html', {'form': form})


def AuthorInfo(request, id):
    tweets = Tweet.objects.filter(author=id)
    counttweets = tweets.count()
    user = MyUser.objects.get(id=id)
    followers = user.followers.all()
    countfollowers = followers.count()
    if request.user.is_authenticated:
        myfollowers = request.user.followers.all()
        if user in myfollowers:
            is_following = True
        else:
            is_following = False
        return render(
                request, 
                'authorinfo.html', {
                'tweets': tweets, 
                'counttweets': counttweets,
                'user': user, 
                'countfollowers': countfollowers,
                'myfollowers': myfollowers,
                'is_following': is_following,
                })    
    return render(
                request, 
                'authorinfo.html', {
                'tweets': tweets, 
                'counttweets':counttweets,
                'user': user,
                'countfollowers': countfollowers,
                })
    
def follow(request, id):
    user = request.user
    follow = MyUser.objects.get(id=id)
    user.followers.add(follow)
    user.save()
    return HttpResponseRedirect(reverse('authorinfo', args={id,}))

def unfollow(request, id):
    user = request.user
    follow = MyUser.objects.get(id=id)
    user.followers.remove(follow)
    user.save()
    return HttpResponseRedirect(reverse('authorinfo', args={id,}))