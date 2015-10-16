from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OfferMission.models import *

def createMission(post, User):
    newMission =  Mission()
    newMission.title = post['title']
    newMission.context = post['context']
    newMission.status = post['status']
    newMission.type = post['type']
    newMission.reward = post['reward']
    newMission.fine = post['fine']
    newMission.deadline = post['deadline']
    newMission.employer = User
    newMission.save()
    return newMission

def createAttachment():
    pass

def offerMethod(request):
    usrname = request.session.get('usrname', None)
    if (usrname is None):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        pass
    return HttpResponse('Offer Mission')