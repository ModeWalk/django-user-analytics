from celery.task import task, periodic_task
from celery.schedules import crontab
from django.contrib.auth.models import User
from django.utils import simplejson
from models import RawTrackingEvent
import logging
logger = logging.getLogger(__name__)


@task(name='user_analytics.set_warning')
def async_set_warning(**kwargs):

    u = User.objects.get(pk=kwargs['user_id'])

    msg = "%s | (%s) %s %s last_login: %s " % (kwargs['message'],
                                     u.username or '',
                                     u.first_name or '',
                                     u.last_name or '',
                                     u.last_login or '')
    logger.warning(msg)

    return

@task(name='user_analytics.register_event')
def async_register_event(**kwargs):

    original_cookie = kwargs.get('cookie', None)

    #check that they cookie has not been tampered with
    from tracking import verify_tracking_key
    cookie = verify_tracking_key(original_cookie)
    if cookie is None:
        if original_cookie == None:
            original_cookie = ''
        logger.warning('cookie %s has been tampered with' % (original_cookie))
        return

    event_name = kwargs.get('event_name', 'UNDEFINED')
    event_time = kwargs.get('event_time', None)

    raw_request = kwargs.get('request', None)

    #Do some filtering before we write to the db.

    # skip favico.ico requests. This case only happens if we are in debug mode
    # and we are serving favicon.ico file using the debug server (since there is no
    # nginx or apache directive that would proxy that to a static file instead

    if kwargs['event_name'] == 'PAGE_VISITED':
        if raw_request is not None:
            if '/favicon.ico' in raw_request['PATH_INFO']:
                return

    raw_request_json = simplejson.dumps(raw_request)

    try:
        tracking_event = RawTrackingEvent()

        tracking_event.event_time = event_time
        tracking_event.name = event_name
        tracking_event.cookie = cookie
        tracking_event.raw_request = raw_request_json

        tracking_event.save()

    except  Exception, exc:
        pass
        async_register_event.retry(exc=exc)

@periodic_task(name='user_analytics.combine_periodic_task', run_every=crontab(hour='0', minute='0', day_of_week='*'))
def async_combine_periodic_task():

    return

