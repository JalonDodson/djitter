from twitter_notifications.models import Notification


def notifications_processor(request):
    if request.user.is_authenticated:
        notifs = len(Notification.objects.filter(to=request.user, unread=True))
    else:
        notifs = 0
    return {"notifs": notifs}
