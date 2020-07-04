from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('authorinfo/<int:id>', views.AuthorInfo, name='authorinfo'),
    path('follow/<int:id>/', views.follow, name='follow'),
    path('unfollow/<int:id>/', views.unfollow, name='unfollow')
]