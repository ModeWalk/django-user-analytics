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


    try:
        tracking_event = RawTrackingEvent()

        tracking_event.event_time = kwargs['event_time']
        tracking_event.name = kwargs['event_name']
        tracking_event.cookie = kwargs['cookie']

        tracking_event.raw_request = simplejson.dumps(kwargs['request'])

        tracking_event.save()

    except  Exception, exc:
        pass
        async_register_event.retry(exc=exc)

@periodic_task(name='user_analytics.combine_periodic_task', run_every=crontab(hour='0', minute='0', day_of_week='*'))
def async_combine_periodic_task():

    return

