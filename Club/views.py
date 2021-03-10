from django.shortcuts import render, get_object_or_404
from .models import resource, clubMeeting
from .forms import clubMeetingForm, resourceForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newMeeting(request):
    form=clubMeetingForm
    if request.method=='POST':
        form=clubMeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=clubMeetingForm()

    else:
        form=clubMeetingForm()
    return render(request, 'Club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=resourceForm
    if request.method=='POST':
        form=resourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=resourceForm()

    else:
        form=resourceForm()
    return render(request, 'Club/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'Club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Club/logoutmessage.html')