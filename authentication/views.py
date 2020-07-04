from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import MyUser
from tweet.models import Tweet
from authentication.forms import LoginForm
from twitteruser.forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from twitterclone import settings
from django.views.generic import View
from django.utils.decorators import method_decorator

# Create your views here.
"""@login_required
def index(request):
    data = Tweet.objects.all().order_by('-time')
    return render(request, 'index.html', {'data': data})"""
class index(View):
    @method_decorator(login_required)
    def get(self, request):
        data = Tweet.objects.all().order_by('-time')
        return render(request, 'index.html', {'data': data})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate( 
                request, 
                username = data['username'], 
                password = data['password']
                )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next' , reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def logoutview(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return HttpResponseRedirect(reverse('homepage'))