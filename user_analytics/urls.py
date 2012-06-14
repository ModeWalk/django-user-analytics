from django.conf.urls.defaults import url, patterns
from user_analytics.views import VerifyView, RegisterEventView
from django.views.decorators.csrf import csrf_view_exempt

urlpatterns = patterns('brand.views',
    url(r'^ua-yb/verify$', VerifyView.as_view(), name='verify'),
    url(r'^ua-yb/register-event$', RegisterEventView.as_view(), name='register_event'),
)