from django.db import models


#class TrackedUser(models.Model):
#    cookie = models.TextField(blank=True,null=True)
#    user_agent = models.TextField(blank=True,null=True)
#    creation_time = models.DateTimeField()


class RawTrackingEvent(models.Model):

    name = models.CharField(max_length=255)
    event_time = models.DateTimeField(blank=False)
    cookie = models.CharField(max_length=32)
    raw_request = models.TextField()
    event_data = models.TextField(null=True, blank=True)


#remote_address = models.IPAddressField()
#    host = models.CharField(max_length=1000)
#    path = models.CharField(max_length=1000)
#    method = models.CharField(max_length=50)
#    uri = models.CharField(max_length=2000)
#    status_code = models.IntegerField()
#    user_agent = models.CharField(max_length=1000,blank=True,null=True)
#    remote_addr = models.IPAddressField()
#    remote_addr_fwd = models.IPAddressField(blank=True,null=True)
#    meta = models.TextField()
#    cookies = models.TextField(blank=True,null=True)
#    get = models.TextField(blank=True,null=True)
#    post = models.TextField(blank=True,null=True)
#    raw_post = models.TextField(blank=True,null=True)
#    is_secure = models.BooleanField()
#    is_ajax = models.BooleanField()
#    user = models.ForeignKey(User,blank=True,null=True)




#class WebRequest(models.Model):
#    time = models.DateTimeField(auto_now_add=True)
#    host = models.CharField(max_length=1000)
#    path = models.CharField(max_length=1000)
#    method = models.CharField(max_length=50)
#    uri = models.CharField(max_length=2000)
#    status_code = models.IntegerField()
#    user_agent = models.CharField(max_length=1000,blank=True,null=True)
#    remote_addr = models.IPAddressField()
#    remote_addr_fwd = models.IPAddressField(blank=True,null=True)
#    meta = models.TextField()
#    cookies = models.TextField(blank=True,null=True)
#    get = models.TextField(blank=True,null=True)
#    post = models.TextField(blank=True,null=True)
#    raw_post = models.TextField(blank=True,null=True)
#    is_secure = models.BooleanField()
#    is_ajax = models.BooleanField()
#    user = models.ForeignKey(User,blank=True,null=True)
