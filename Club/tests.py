from django.test import TestCase
from django.contrib.auth.models import User
from .models import clubMeeting, meetingMinutes, event, resource
import datetime
# Create your tests here.
class clubMeetingtest(TestCase):
    def setUp(self):
        self.type=clubMeeting(meetingtitle='Tech Fieldtrip')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Tech Fieldtrip')

    def test_tablename(self):
        self.assertEqual(str(clubMeeting._meta.db_table), 'clubmeeting')

class meetingMinutestest(TestCase):
    def setUp(self):
        self.type=meetingMinutes(meetingminutes='30 mins')
        self.user=User(username='user1')
        self.meetingid=clubMeeting(meetingtitle='Tech Fieldtrip', meetingdate=datetime.date(2021, 3, 10), meetingtime=datetime.time(12, 00, 00), meetinglocation='SCC', meetingagenda='going on fieldtrip')

    def test_typestring(self):
        self.assertEqual(str(self.type), '30 mins')

#error:meetingMinutes has no meetingid
#I don't know why this happens and would love some help, thank you

    def test_tablename(self):
        self.assertEqual(str(meetingMinutes._meta.db_table), 'meetingminutes')

class resourcetest(TestCase):
    def setUp(self):
        self.type=resource(resourcename='Python Cheat Sheet')
        self.userid=User(username='user1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Python Cheat Sheet')

    def test_tablename(self):
        self.assertEqual(str(resource._meta.db_table), 'resource')

class eventtest(TestCase):
    def setUp(self):
        self.type=event(eventtitle='Python Meeting')
        self.userid=User(username='user1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Python Meeting')

    def test_tableneame(self):
        self.assertEqual(str(event._meta.db_table), 'event')