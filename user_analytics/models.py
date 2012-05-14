from django.db import models
#from utils import TwoWayDic
#from django.contrib.auth.signals import user_logged_in, user_logged_out
#from user_analytics.tracking import register_event, set_warning

#TrackingEvent = TwoWayDic({
#    'COOKIE_SET' : 1,
#    'USER_LOGGED_IN': 2,
#    'USER_LOGGED_OUT' : 3,
#    'PAGE_VISITED' : 4
#})

class TrackingEvent:
    COOKIE_SET = 1
    USER_LOGGED_IN = 2
    USER_LOGGED_OUT = 3
    PAGE_VISITED = 4

    TRACKING_EVENT_CHOICES = (
        (COOKIE_SET, 'Cookie Set'),
        (USER_LOGGED_IN, 'User Logged In'),
        (USER_LOGGED_OUT, 'User Logged Out'),
        (PAGE_VISITED, 'Page visited'),
    )


class TrackedUser(models.Model):
    cookie = models.TextField(blank=True,null=True)
    user_agent = models.TextField(blank=True,null=True)






#class WebRequest(models.Model):
#    time = models.DateTimeField(auto_now_add=True)
#    host = models.CharField(max_length=1000)
#    path = models.CharField(max_length=1000)
#    method = models.CharField(max_length=50)
#    uri = models.CharField(max_length=2000)
#    status_code = models.IntegerField()
#    user_agent = models.CharField(max_length=1000,blank=True,null=True)
#    remote_addr = models.IPAddressField()
#    remote_addr_fwd = models.IPAddressField(blank=True,null=True)
#    meta = models.TextField()
#    cookies = models.TextField(blank=True,null=True)
#    get = models.TextField(blank=True,null=True)
#    post = models.TextField(blank=True,null=True)
#    raw_post = models.TextField(blank=True,null=True)
#    is_secure = models.BooleanField()
#    is_ajax = models.BooleanField()
#    user = models.ForeignKey(User,blank=True,null=True)
