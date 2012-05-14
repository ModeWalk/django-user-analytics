from celery.task import task, periodic_task
from celery.schedules import crontab
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)


@task(name='user_analytics.set_warning')
def async_set_warning(**kwargs):

    print 'async_set_warning'

    u = User.objects.get(pk=kwargs['user_id'])

    msg = "%s | (%s) %s %s last_login: %s " % (kwargs['message'],
                                     u.username or '',
                                     u.first_name or '',
                                     u.last_name or '',
                                     u.last_login or '')
    logger.warning(msg)

    return

@task(name='user_analytics.process_event')
def async_process_event(**kwargs):

    print 'async_process_event'

    tracking_event = kwargs['tracking_event']

    if (kwargs['force_write'] == True):
        #print 'Registering event ' + TrackingEvent.reverse(tracking_event)
        #TODO: Write to db code
        return


    #TODO: analyze URL
    #print 'Analyzing event ' + TrackingEvent.reverse(tracking_event)
    print kwargs['request']


    #TODO: Write to db code


    #except  Exception, exc:
    #    pass

    #   print "Restarting..."
    #    async_process_event.retry(exc=exc)

@periodic_task(name='user_analytics.combine_periodic_task', run_every=crontab(hour='0', minute='0', day_of_week='*'))
def async_combine_periodic_task():

    return

