from django.views.generic import View
from django.http import HttpResponse
from tracking import register_event

class VerifyView(View):
    '''
    View called by javascript to verify that cookies are enabled along with javascript
    '''

    def post(self, request, *args, **kwargs):

        tracking_id = self.request.COOKIES.get('yb_user', None)
        register_event(tracking_id, event_name='VERIFY_COOKIE', request=self.request)
        response = HttpResponse('Verified')
        response.delete_cookie('yb_verify')

        return response

