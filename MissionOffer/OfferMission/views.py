import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OfferMission.models import *
from django.core.files import File
from django.core.servers.basehttp import FileWrapper
from datetime import datetime

def createMissionMethod(request, user):  # 创建一个Mission但是没发布，且没有和Attachment绑定
    newMission =  Mission()
    newMission.title = request.POST['title']
    newMission.context = request.POST['context']
    newMission.status = '0'
    newMission.type = request.POST['type']
    newMission.reward = int(request.POST['reward'])
    newMission.fine = int(request.POST['fine'])
    if newMission.reward < 0 or newMission.reward <0:
        return (1,None)
    if newMission.reward > user.money:
        return (2,None)
    user.money -= newMission.reward
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']
    hour = request.POST['hour']
    minute = request.POST['minute']
    newMission.deadline = datetime(year=int(year),month=int(month),day=int (day),hour=int (hour),minute=int (minute))
    print(newMission.deadline)
    if newMission.deadline < datetime.now():
        return (3,None)
    newMission.employer = user
    newMission.save()
    user.save()
    return (0,newMission)

def uploadFileMethod(request):  # 上传文件
    try:
        files = request.FILES.getlist('multipleFileUpload')
        print (len(files))
        for f in files:
            print (f.name)
            newAttachment = Attachment()
            newAttachment.files = f
            newAttachment.originName = f.name
        return newAttachment
    except:
        return None
    # return render_to_response('file.html')


def createAttachmentMethod(request, mission):  # 整合创建附件
    if  (request.method == 'POST'):
        try:
            files = request.FILES.getlist('multipleFileUpload')
            print (len(files))
            for f in files:
                print (f.name)
                newAttachment = Attachment()
                newAttachment.files = f
                newAttachment.originName = f.name
                newAttachment.belongTo = mission
                newAttachment.save()
            return newAttachment
        except:
            return None
        # return newAttachment

def offerMethod(request):  # 发布任务，这个方法实现整个任务的发布功能
    usrname = request.session.get('usrname', None)
    if (usrname is None):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        nowUser = User.objects.filter(usrname__exact=usrname)
        if nowUser:
            nowUser = nowUser[0]
            print(request.POST)
            nowMission = createMissionMethod(request,nowUser)
            if nowMission[0] == 1:
                return HttpResponse('赏金和押金必须为正数！')
            if nowMission[0] == 2:
                return HttpResponse('账户余额不足！')
            if nowMission[0] == 3:
                return HttpResponse('截止日期已过！')
            if nowMission[0] == 0:
                nowMission = nowMission[1]
                # print(nowMission.offerTime)
                # print(datetime.utcnow())
                # print(nowMission.deadline)
                createAttachmentMethod(request,nowMission)
                return HttpResponse('Offer Mission successfully!')
            else:
                return HttpResponse('Fail!')
        else:
            return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/index')
    # return render_to_response('offerMissionFramework.html',{})
    # return render_to_response('publish.html',{})

def viewMissionMethod(request, missionID):
    print(missionID)
    mission = Mission.objects.filter(id__exact=24)
    print(mission)
    if (mission):
        mission = mission[0]
        return render_to_response('viewMission.html',{'mission':mission})
    else:
        return HttpResponse('任务不存在！')

def downloadFileMethod(request):
    nowAttchment = Attachment.objects.last()
    nowFile = nowAttchment.files  # 先写了下载最后一个上传的文件的实现，之后需要实现和任务的链接
                                               # 还有需要判断当前下载的用户是否为任务接受者？
    def readFile(f, buf_size=262144):  # 大文件下载，设定缓存大小
        while True:  # 循环读取
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()
    # 'attachment; filename='
    response = HttpResponse(readFile(nowFile), content_type='APPLICATION/OCTET-STREAM')  # 设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开
    response['Content-Encoding'] = 'unicode'
    response['Content-Disposition'] = 'attachment; filename='+ nowAttchment.originName.encode('utf-8')  # 设定传输给客户端的文件名称
    response['Content-Length'] = nowFile.size  # 传输给客户端的文件大小
    return response
