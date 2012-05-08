from datetime import datetime
import uuid
from tasks import async_set_warning, async_process_event
from utils import massage_request


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
        'request' : massage_request(request)
        }

    async_process_event.apply_async(args=[], kwargs=params)


def set_warning(message='', user_id=None):
    async_set_warning.apply_async(args=[], kwargs = {
        'message' : message,
        'user_id' : user_id,
        })
