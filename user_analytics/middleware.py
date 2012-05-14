from models import TrackingEvent
from tracking import generate_new_tracking_key, register_event, process_event


#TODO: think about how this is going to be augmented when using varnish

class UserTrackingMiddleware(object):

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        """
        Only record when we return HTML pages. Set a cookie if not set
        """

        if 'text/html' in response.get('Content-Type', ''):

            tracked_user = None

            if not request.COOKIES.has_key( 'yb_user' ):

                tracked_user = generate_new_tracking_key()

                response.set_cookie('yb_user', tracked_user)

                register_event(tracking_id=tracked_user, tracking_event=TrackingEvent.COOKIE_SET)

            else:
                tracked_user = request.COOKIES[ 'yb_user' ]


            process_event(tracking_id=tracked_user, tracking_event=TrackingEvent.PAGE_VISITED, request=request)


        return response
