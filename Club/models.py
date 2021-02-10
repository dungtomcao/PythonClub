from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class clubMeeting(models.Model):
    meetingtitle=models.CharField(max_length=225)
    meetingdate=models.DateField()
    meetingtime= models.TimeField(auto_now=False, auto_now_add=False)
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='clubmeeting'
        verbose_name_plural='clubmeetings'

class meetingMinutes(models.Model):
    meetingid=models.ForeignKey(clubMeeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    meetingminutes=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField(null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.TextField(null=True, blank=True)
    eventdescription=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'
