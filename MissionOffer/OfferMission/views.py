import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OfferMission.models import *
from django.core.files import File

def createMissionMethod(post, user):
    newMission =  Mission()
    newMission.title = post['title']
    newMission.context = post['context']
    newMission.status = post['status']
    newMission.type = post['type']
    newMission.reward = post['reward']
    newMission.fine = post['fine']
    newMission.deadline = post['deadline']
    newMission.employer = user
    newMission.save()
    return newMission

def uploadFileMethod(request):
    if  (request.method == 'POST'):
        files = request.FILES.getlist('multipleFileUpload')
        print (len(files))
        for f in files:
            newAttachment = Attachment()
            newAttachment.files = f
            newAttachment.save()

        return HttpResponse('success')
    return render_to_response('file.html')


def createAttachmentMethod(request, mission):
    pass


def offerMethod(request):
    usrname = request.session.get('usrname', None)
    if (usrname is None):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        pass
    return HttpResponse('Offer Mission')