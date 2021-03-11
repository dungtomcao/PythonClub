from django.test import TestCase
from django.contrib.auth.models import User
from .models import clubMeeting, meetingMinutes, event, resource
import datetime
from django.urls import reverse, reverse_lazy

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

    def test_tablename(self):
        self.assertEqual(str(meetingMinutes._meta.db_table), 'meetingminutes')
#update: 'meetingMinutes has no meetingid' error troubleshooted 
#__str__ in meetingMinutes was changed from self.meetingid to self.meetingminutes
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

class new_resource_authentication_test(TestCase):
    def setUp(self):
        self.type=resource(resourcename='resource1', resourcetype='type1', resourceurl='url1', dateentered=datetime.date(2021, 1, 2),userid=User(username='testuser1'), resourcedescription='a resource')
        self.test_user=User.objects.create(username='testuser1', password='P@ssw0rd1')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newResource/')

'''ERROR: test_logged_in_uses_correct_template (Club.tests.new_resource_authentication_test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/elisacao/Desktop/SCC doc/IT112/djangoprojects/PythonClub_W2021/Club/tests.py", line 65, in test_logged_in_uses_correct_template
    self.assertEqual(str(response.context['user']), 'testuser1')
TypeError: 'NoneType' object is not subscriptable'''

'''I have been doing research on why this error happens and how to fix it, as well as trying out a couple solutions to no avail. Please help. Thank you'''
    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newresource.html')