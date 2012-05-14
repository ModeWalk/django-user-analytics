from datetime import datetime
import uuid
from tasks import async_set_warning, async_process_event
from utils import massage_request
from django.contrib.auth.signals import user_logged_in, user_logged_out
from models import TrackingEvent


def generate_new_tracking_key():
    tracking_key = str(uuid.uuid1())
    return tracking_key


def register_event(tracking_id=None, tracking_event=None, request=None):

    process_event(tracking_id = tracking_id,
        tracking_event = tracking_event,
        request = request,
        force_write=True
    )

def process_event(tracking_id=None, tracking_event=None, request=None, force_write=False):

    params = {
        'force_write' : False,
        'event_time' : datetime.now(),
        'tracking_event' : tracking_event,
        }

    if not request is None:
        params['request'] = massage_request(request)

    async_process_event.apply_async(args=[], kwargs=params)


def set_warning(message='', user_id=None):
    async_set_warning.apply_async(args=[], kwargs = {
        'message' : message,
        'user_id' : user_id,
        })



def register_user_logged_in(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_IN
    """

    if 'yb_user' in request.COOKIES:
        tracked_user = request.COOKIES[ 'yb_user' ]
        register_event(tracked_user, TrackingEvent.USER_LOGGED_IN, user)
    else:
        set_warning(message="User logged-in but doesn't have cookie set.", user_id = user.id)

user_logged_in.connect(register_user_logged_in, dispatch_uid="USER_ANALYTICS_USER_LOGGED_IN")

def register_user_logged_out(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_OUT
    """
    if 'yb_user' in request.COOKIES:
        tracked_user = request.COOKIES[ 'yb_user' ]
        register_event(TrackingEvent.USER_LOGGED_IN)
    else:
        set_warning(message="User logged-out but doesn't have cookie set.", user_id = user.id)

user_logged_out.connect(register_user_logged_out, dispatch_uid="USER_ANALYTICS_USER_LOGGED_OUT")