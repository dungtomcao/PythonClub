from django import forms
from .models import resource, clubMeeting

class clubMeetingForm(forms.ModelForm):
    class Meta:
        model=clubMeeting
        fields='__all__'

class resourceForm(forms.ModelForm):
    class Meta:
        model=resource
        fields='__all__'