from django.db import models
from Login.models import User


class Mission(models.Model):
    statusChoices = (('0', u'待接收'),('1', u'进行中'),('2','待审核'),('3', u'已完成'))
    typeChoices = (('0', u'寻找失物'),('1', u'食堂带饭'),('2', u'超市购物'),('3',u'文印中心'),('4',(u'校外任务')),('5',(u'其他')))
    status = models.CharField(max_length=20,choices=statusChoices,default='0')  # 任务状态
    type = models.CharField(max_length=20,choices=typeChoices,default='0')
    title = models.CharField(max_length=50)  # 标题
    context = models.TextField(max_length=200)  # 任务描述
    reward = models.FloatField()  # 奖金
    fine = models.FloatField()  # 罚款
    offerTime = models.DateTimeField(auto_now_add=True)  # 发布时间
    deadline = models.DateTimeField()  # 截止期限
    employer = models.ForeignKey(User, related_name='missionEmployer')  # 雇主，即任务发布人
    employee = models.ForeignKey(User, related_name='missionEmployee',null=True)  # 雇员，即任务接受人

    def __str__(self):
        return str(self.id) +'-'+ self.title

    class Meta:
        ordering = ['-offerTime']


class Attachment(models.Model):  # 任务附件，感觉需要一个字段存原始文件名，待实现
    originName = models.CharField(max_length=256,null=True)  # 原始文件名
    files = models.FileField(upload_to='uploadFiles/Attachments')  # 文件
    belongTo = models.ForeignKey(Mission,null=True)  # 所属任务

    def __str__(self):
        return self.files.name