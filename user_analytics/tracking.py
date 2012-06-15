from datetime import datetime
import uuid
from tasks import async_set_warning, async_register_event
from utils import massage_request
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings

USER_ANALYTICS_ENABLED = getattr(settings, "USER_ANALYTICS_ENABLED", True)

import django

if django.get_version() < '1.4':
    from user_analytics.backported.signing import Signer, BadSignature
else:
    from django.core.signing import Signer, BadSignature

signer = Signer()

def generate_new_tracking_key():
    tracking_key = str(uuid.uuid1()).replace('-','')
    return signer.sign(tracking_key)

def verify_tracking_key(key):
    try:
        value = signer.unsign(key)
        return value
    except  BadSignature:
        return None


def register_event(tracking_id=None, event_name=None, request=None, event_data=None):

    if not USER_ANALYTICS_ENABLED:
        return

    params = {
        'cookie' : tracking_id,
        'event_time' : datetime.now(),
        'event_name' : event_name,
        'event_data' : event_data,
        }

    if not request is None:
        params['request'] = massage_request(request)

    async_register_event.apply_async(args=[], kwargs=params)


def set_warning(message='', user_id=None):

    if not USER_ANALYTICS_ENABLED:
        return

    async_set_warning.apply_async(args=[], kwargs = {
        'message' : message,
        'user_id' : user_id,
        })


def register_user_logged_in(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_IN
    """

    if 'yb_user' in request.COOKIES:
        cookie = request.COOKIES[ 'yb_user' ]
        register_event(tracking_id=cookie, event_name='USER_LOGGED_IN', request=request)
    else:
        set_warning(message="User logged-in but doesn't have cookie set.", user_id = user.id)

user_logged_in.connect(register_user_logged_in, dispatch_uid="USER_ANALYTICS_USER_LOGGED_IN")

def register_user_logged_out(sender, request, user, **kwargs):
    """
    A signal receiver which triggers USER_LOGGED_OUT
    """
    if 'yb_user' in request.COOKIES:
        cookie = request.COOKIES[ 'yb_user' ]
        register_event(tracking_id=cookie, event_name='USER_LOGGED_OUT', request=request)
    else:
        set_warning(message="User logged-out but doesn't have cookie set.", user_id = user.id)

user_logged_out.connect(register_user_logged_out, dispatch_uid="USER_ANALYTICS_USER_LOGGED_OUT")