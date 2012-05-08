#from django.db import models
from utils import TwoWayDic
from django.contrib.auth.signals import user_logged_in, user_logged_out
from tracking import register_event, set_warning

TrackingEvent = TwoWayDic({
    'COOKIE_SET' : 1,
    'USER_LOGGED_IN': 2,
    'USER_LOGGED_OUT' : 3,
    'PAGE_VISITED' : 4
})


def register_user_logged_in(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_IN
    """

    if 'tr_user' in request.COOKIES:
        tracked_user = request.COOKIES[ 'tr_user' ]
        register_event(tracked_user, TrackingEvent.USER_LOGGED_IN, user)
    else:
        set_warning(message="User logged-in but doesn't have cookie set.", user_id = user.id)


user_logged_in.connect(register_user_logged_in)

def register_user_logged_out(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_OUT
    """
    if 'tr_user' in request.COOKIES:
        tracked_user = request.COOKIES[ 'tr_user' ]
        register_event(TrackingEvent.USER_LOGGED_IN)
    else:
        set_warning(message="User logged-out but doesn't have cookie set.", user_id = user.id)

user_logged_out.connect(register_user_logged_out)





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
