import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OfferMission.models import *
from datetime import datetime


def createMissionMethod(request, user):  # 创建一个Mission但是没发布，且没有和Attachment绑定
    newMission =  Mission()
    newMission.title = request.POST['title']
    if newMission.title == '':
        return ('标题不能为空！',None)
    newMission.context = request.POST['context']
    if newMission.context == '':
        return ('描述不能为空！',None)
    newMission.status = '0'
    newMission.type = request.POST['type']
    if newMission.type == '任务类型':
        return ('类型不能为空！',None)
    if request.POST['reward'] == '':
        return ('赏金不能为空！',None)
    if request.POST['fine'] == '':
        return ('押金不能为空！',None)
    newMission.reward = int(request.POST['reward'])
    newMission.fine = int(request.POST['fine'])
    if newMission.reward < 0 or newMission.reward <0:
        return ('赏金和押金必须为正数！',None)
    if newMission.reward > user.money:
        return ('账户余额不足！',None)
    user.money -= newMission.reward
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']
    hour = request.POST['hour']
    minute = request.POST['minute']
    if year=='0' or month=='0' or day=='0' or hour=='0' or minute=='0':
        return ('日期信息不能为空！',None)
    try :
        newMission.deadline = datetime(year=int(year),month=int(month),day=int (day),hour=int (hour),minute=int (minute))
    except :
        return ('日期信息错误！',None)
    print(newMission.deadline)
    if newMission.deadline < datetime.now():
        return ('截止日期已过！',None)
    newMission.employer = user
    newMission.save()
    user.save()
    return ('',newMission)

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
            # print (len(files))
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
            nowMission = createMissionMethod(request,nowUser)
            if nowMission[0]:
                return render_to_response('offerResult.html',{'reason':nowMission[0]})
            if not nowMission[0]:
                nowMission = nowMission[1]
                # print(nowMission.offerTime)
                # print(datetime.utcnow())
                # print(nowMission.deadline)
                createAttachmentMethod(request,nowMission)
                return render_to_response('offerResult.html',{'reason':'Offer Mission successfully!'})
                # return HttpResponse('Offer Mission successfully!')
            else:
                return render_to_response('offerResult.html',{'reason':'Fail!'})
                # return HttpResponse('Fail!')
        else:
            return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/index')
    # return render_to_response('offerMissionFramework.html',{})
    # return render_to_response('publish.html',{})

def viewMissionMethod(request, missionID):
    print(int(missionID))
    mission = Mission.objects.filter(id__exact=int(missionID))
    print(mission)
    if (mission):
        mission = mission[0]
        usrname = request.session.get('usrname', '')
        buttonMark = 0
        if usrname:
            nowUser = User.objects.filter(usrname__exact=usrname)[0]

            if mission.status == '0':
                if mission.employer != nowUser:
                    buttonMark = 1
            if mission.status == '1':
                if mission.employee == nowUser:
                    buttonMark = 2
                else:
                    buttonMark = 0
            if mission.status == '2':
                if mission.employer == nowUser:
                    buttonMark = 3
                else:
                    buttonMark = 0
            if mission.status == '3':
                buttonMark = 0

            if request.method == 'POST':
                print('***************')
                print(int(missionID))
                print('***************')
                if buttonMark == 1:
                    if nowUser.money < mission.fine:
                        return HttpResponse('资金不足以支付押金！')
                    nowUser.money -= mission.fine
                    nowUser.save()
                    mission.employee = nowUser
                    mission.status = '1'
                    mission.save()
                elif buttonMark == 2:
                    mission.status = '2'
                    mission.save()
                elif buttonMark == 3:
                    mission.status = '3'
                    mission.save()
                    employee=mission.employee
                    employee.money += (mission.reward + mission.fine)
                    employee.save()
                return HttpResponseRedirect('/mission/'+missionID+'/')


        leftDays = (mission.deadline - datetime.now()).days
        attachmentList = mission.attachment_set.all()
        # print(attachmentList)
        # print(leftDays)
        print(buttonMark)
        # return render_to_response('viewMission.html',{'mission':mission})
        return render_to_response('taskdetails.html',{'usrname': usrname,
                                                      'mission':mission,
                                                      'leftDays':leftDays,
                                                      'attachmentList':attachmentList,
                                                      'buttonMark':buttonMark})
    else:
        return HttpResponse('任务不存在！')

def downloadFileMethod(request,attachmentID):
    print (int(attachmentID))
    nowAttchment = Attachment.objects.filter(id__exact=int(attachmentID))
    if not nowAttchment:
        return HttpResponse('文件没找到!')
    nowAttchment = nowAttchment[0]
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
    response['Content-Encoding'] = 'utf-8'
    response['Content-Disposition'] = 'attachment; filename='+ nowAttchment.originName  # 设定传输给客户端的文件名称
    response['Content-Length'] = nowFile.size  # 传输给客户端的文件大小
    return response
