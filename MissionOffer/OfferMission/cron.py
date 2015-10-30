__author__ = 'wangzhuo'

from Login.models import *
from OfferMission.models import *
from datetime import datetime

def tryUseCrontab():
    print('############')
    ml = Mission.objects.last()
    ml.title = 'Success'
    ml.save()

def tryUseCrontab2():
    print('############')
    ml = Mission.objects.last()
    ml.title = 'Success@@@@@@@@'
    ml.save()

def deadlineMethod():
    missionList = Mission.objects.all()
    for i in missionList:
        if i.deadline >= datetime.now() and i.status != '4':
            i.status = '4'
            i.save()
            employer = i.employer
            employer.money += (i.fine + i.reward)
            employer.save()
