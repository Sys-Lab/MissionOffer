from django.db import models
from Login.models import User


class Mission(models.Model):
    status = models.CharField(max_length=10,          # 任务状态
                              choices=((0, u'待接收'),
                                       (1, u'进行中'),
                                       (2, u'已完成')))
    title = models.CharField(max_length=50)  # 标题
    context = models.TextField(max_length=200)  # 任务描述
    reward = models.FloatField()  # 奖金
    fine = models.FloatField()  # 罚款
    offerTime = models.DateTimeField(auto_created=True)  # 发布时间
    deadline = models.DateTimeField()  # 截止期限
    employer = models.ForeignKey(User, related_name='missionEmployer')  # 雇主，即任务发布人
    employee = models.ForeignKey(User, related_name='missionEmployee')  # 雇员，即任务接受人

    def __str__(self):
        return self.title
