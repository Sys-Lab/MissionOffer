import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OfferMission.models import *
from django.core.files import File
from django.core.servers.basehttp import FileWrapper


def createMissionMethod(post, user):  # 创建一个Mission但是没发布，且没有和Attachment绑定
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

def uploadFileMethod(request):  # 上传文件
    if  (request.method == 'POST'):
        files = request.FILES.getlist('multipleFileUpload')
        print (len(files))
        for f in files:
            print (f.name)
            newAttachment = Attachment()
            newAttachment.files = f
            newAttachment.originName = f.name
            newAttachment.save()
        return HttpResponse('success')
    return render_to_response('file.html')


def createAttachmentMethod(request, mission):  # 整合创建附件
    pass

def offerMethod(request):  # 发布任务，这个方法实现整个任务的发布功能
    usrname = request.session.get('usrname', None)
    if (usrname is None):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        pass
    return HttpResponse('Offer Mission')

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
