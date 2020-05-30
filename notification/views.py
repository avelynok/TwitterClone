from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Notification
from twitteruser.models import MyUser

# Create your views here.
def notification(request):
    receiver = request.user
    notifications= Notification.objects.filter(receiver = receiver, received=False)
    for notification in notifications:
        notification.received = True
        notification.save()
    return render(request, 'notifications.html', { 'notifications': notifications, 'receiver':receiver})