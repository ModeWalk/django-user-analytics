from django.conf.urls.defaults import url, patterns
from user_analytics.views import VerifyView
from django.views.decorators.csrf import csrf_view_exempt

urlpatterns = patterns('brand.views',
    url(r'^ua-yb/verify$', csrf_view_exempt(VerifyView.as_view()), name='verify'),
)