from tracking import generate_new_tracking_key, register_event


class UserTrackingMiddleware(object):

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        """
        Only record when we return HTML pages. Set a cookie if not set
        """

        if 'text/html' in response.get('Content-Type', ''):

            tracked_user = None

            if 'yb_user' not in request.COOKIES:

                tracked_user = generate_new_tracking_key()

                response.set_cookie('yb_user', tracked_user)

                register_event(tracking_id=tracked_user, event_name='COOKIE_SET', request=request)

                #set javascript callback behavior to check if the user has disabled cookies
                response.set_cookie('yb_verify', tracked_user)

            else:
                tracked_user = request.COOKIES[ 'yb_user' ]


            register_event(tracking_id=tracked_user, event_name='PAGE_VISITED', request=request)


        return response
