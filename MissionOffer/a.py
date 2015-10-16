from Login.models import *
from OfferMission.models import *
from datetime import datetime
un = User.objects.all()[0]
newMission = Mission()
newMission.title = '买asdf饭'
newMission.context = '买asdfsad两份'
newMission.reward = 10.002
newMission.fine = 250
newMission.deadline = datetime.now()
newMission.employer = un
newMission.save()
