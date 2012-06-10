from django.contrib import admin
from models import RawTrackingEvent


class RawTrackingEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'cookie', 'event_time', 'raw_request')
    date_hierarchy = 'event_time'

admin.site.register(RawTrackingEvent, RawTrackingEventAdmin)