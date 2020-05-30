from django.urls import path
from tweet import views

urlpatterns = [
    path('add_tweet/<int:id>/', views.add_tweet, name='add_tweet'),
    path('tweet/<int:id>/', views.tweet_detail, name='tweet_detail'),
]