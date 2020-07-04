from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='homepage'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview')
    
]