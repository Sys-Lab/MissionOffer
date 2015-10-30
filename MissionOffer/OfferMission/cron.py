__author__ = 'wangzhuo'

from Login.models import *
from OfferMission.models import *

def deadlineMethod():
    print('############')
    ml = Mission.objects.last()
    ml.title = 'Success'
    ml.save()