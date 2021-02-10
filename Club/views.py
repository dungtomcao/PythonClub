from django.shortcuts import render, get_object_or_404
from .models import resource, clubMeeting

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
    resource_list=resource.objects.all() 
    return render(request, 'Club/resource.html', {'resource_list': resource_list})

def meetings(request):
    meeting_list=clubMeeting.objects.all()
    return render(request, 'Club/meeting.html', {'meeting_list': meeting_list})

def meetingdetails(request, id):
    meeting=get_object_or_404(clubMeeting, pk=id)
    return render(request, 'Club/meetingdetail.html', {'meeting' : meeting})
