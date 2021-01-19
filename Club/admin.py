from django.contrib import admin

# Register your models here.
from .models import clubMeeting, meetingMinutes, resource, event

admin.site.register(clubMeeting)
admin.site.register(meetingMinutes)
admin.site.register(resource)
admin.site.register(event)