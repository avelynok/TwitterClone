from django.urls import path
from . import views

urlpatterns = [
    path('notification/', views.notification.as_view(), name='notification')
]