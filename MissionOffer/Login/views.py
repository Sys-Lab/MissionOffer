from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from Login.forms import *
from Login.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader
from random import random
from MissionOffer.settings import *
from OfferMission.models import *
import hashlib


def loginCheckMethod(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        uf = LoginForm(request.POST)
        if uf.is_valid():
            un = uf.cleaned_data['UN']
            pw = uf.cleaned_data['PW']
            nowUser = User.objects.filter(usrname__exact=un, password__exact=pw)
            print(nowUser)
            result = {}
            result['success'] = False
            result['reason'] = '用户名或密码错误'
            if nowUser:  # 登录成功
                nowUser = nowUser[0]
                if not nowUser.isActive:
                    result['reason'] = '用户未激活'
                    print('用户未激活')
                    # return HttpResponse()
                    return JsonResponse(result)

                result['success'] = True
                result['reason'] = '登录成功'
                request.session['usrname'] = un
                if request.POST['AUTO'] == 'off':
                    print('@@@@@@@@@@')
                    request.session.set_expiry(0)
                return JsonResponse(result)
                # return HttpResponseRedirect('/index')
            else:  # 先在终端输出错误，之后再编写在网页上提示错误的功能
                print('用户名或密码错误')
                # return HttpResponse()
                return JsonResponse(result)

def loginMethod(request):
    if 'usrname'in request.session:
        del request.session['usrname']
    return render_to_response('login.html', {})

def createNewUser(post):

    newUser = User()  # 创建新用户，加入到数据库中。
    newUser.usrname = post['nickname']
    newUser.password = post['password']
    newUser.idNumber = post['student_number']
    newUser.email = post['usrname']
    newUser.sex = post['sex']
    newUser.phonenumber = post['phone_number']
    newUser.eval = post['introduce']
    newUser.authKey = hashlib.sha1(str(random()).encode('utf-8')).hexdigest()
    newUser.isActive = False

    # emailContent = loader.render_to_string('Email.html')
    # print(emailContent)
    subject = 'MissionOffer register e-mail'
    fromEmail = 'missionoffer@sina.com'
    toEmail = [newUser.email]
    t = loader.get_template('Email.html')
    activateUrl = MY_SITE_URL+'/register/activate/'+newUser.authKey
    htmlContent = t.render(Context({'activateUrl':activateUrl}))
    msg = EmailMultiAlternatives(subject, htmlContent, fromEmail, toEmail)
    msg.attach_alternative(htmlContent, "text/html")
    try :
        msg.send()
    except:
        print ('Email Error')
        return None
    newUser.save()
    # send_mail('MissionOffer register e-mail',
    #           emailContent,
    #           #'This is a test e-mail from MissionOffer website.',
    #           # 'http://192.168.1.115:8000/register/emailAuth/'
    #           # +newUser.authKey,
    #           'missionoffer@sina.com',
    #           [newUser.email],
    #           fail_silently=False)
    return newUser

def activateMethod(request, authKey):
    print(authKey)
    nowUser = User.objects.filter(authKey__exact=authKey)
    if nowUser:
        nowUser = nowUser[0]
        nowUser.isActive = True
        nowUser.authKey = None
        nowUser.save()
        return HttpResponse('激活成功！')
    else:
        return HttpResponse('激活失败！')

def registerMethod(request):
    if 'usrname'in request.session:
        del request.session['usrname']
    if request.method == 'POST':
        print(request.POST)
        if 'submit' in request.POST:  # 先在终端输出错误，之后再编写在网页上提示错误的功能

            if len(request.POST['read']) <= 0:  # 没输入用户名
                print('请遵守条款！')
                return render_to_response('register.html', {})
            if len(request.POST['nickname']) <= 0:  # 没输入用户名
                print('请输入用户名！')
                return render_to_response('register.html', {})
            if len(request.POST['password']) <= 0:  # 没输入密码
                print('请输入密码！')
                return render_to_response('register.html', {})
            if len(request.POST['usrname']) <= 0:  # 没输入邮箱
                print('请输入邮箱！')
                return render_to_response('register.html', {})
            if len(request.POST['sex']) <= 0:  # 没输入性别
                print('请输入性别！')
                return render_to_response('register.html', {})
            if request.POST['password'] != request.POST['repassword']:  # 密码不一致
                print('密码不一致')
                return render_to_response('register.html', {})
            findList = User.objects.filter(usrname=request.POST['nickname'])
            if len(findList) > 0:  # 用户已存在
                print('用户已存在')
                return render_to_response('register.html', {})
            findList = User.objects.filter(email=request.POST['usrname'])
            if len(findList) > 0:  # 邮箱已存在
                print('邮箱已存在')
                return render_to_response('register.html', {})

            newUser = createNewUser(request.POST)
            if not newUser:
                return HttpResponse('邮箱发送失败，请重新注册！')
            # request.session['usrname'] = request.POST['usrname']
            return HttpResponseRedirect('/index')
            # return render_to_response('afterregister.html',request.POST)
    return render_to_response('register.html', {})

def toIndexMethod(request):
    return HttpResponseRedirect('/index/6')

def getMissionListMethod(request):
    type = request.POST['type']
    status = request.POST['status']
    if type == '' and status == '':
        list = Mission.objects.filter()
    else:
        list = Mission.objects.filter(type__exact=type,status__exact=status)
    return list
    # print(list)


def indexMethod(request,type,status):
    print(type,status)
    if status=='':
        url = '/index/'+type+'/6/'
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        missionList = getMissionListMethod(request)
    # if type=='0':
    if type=='6' and status == '6':
        print('#########')
        missionList = Mission.objects.filter()
    elif type=='6':
        missionList = Mission.objects.filter(status__exact=status)
    elif status=='6':
        missionList = Mission.objects.filter(type__exact=type)
    else:
        missionList = Mission.objects.filter(type__exact=type,status__exact=status)
    # for i in missionList:
    #     i.status = i.get_status_display()
    #     i.type = i.get_type_display()
    usrname = request.session.get('usrname', '')
    return render_to_response('framework.html',{'usrname': usrname,'missionList':missionList,'type':type})

def logoutMethod(request):
    del request.session['usrname']
    return HttpResponseRedirect('/index')

def userCenterMethod(request):
    usrname = request.session.get('usrname', '')
    if usrname == '':
        return HttpResponseRedirect('/login/')
    nowUser = User.objects.filter(usrname__exact=usrname)
    if not nowUser:
        return HttpResponse('Error!')
    nowUser = nowUser[0]
    myMissionList = nowUser.missionEmployer.all()
    acMissionList = nowUser.missionEmployee.all()
    mylen = len(myMissionList)
    aclen = len(acMissionList)
    trueList = []
    acList = []
    for i in range(mylen):
        if i % 2 ==1:
            trueList.append((myMissionList[i],1))
        else:
            trueList.append((myMissionList[i],0))
    for i in range(aclen):
        if i % 2 ==1:
            acList.append((acMissionList[i],1))
        else:
            acList.append((acMissionList[i],0))
    return render_to_response('usercenter.html',{'usrname':usrname,
                                                 'user':nowUser,
                                                 'myMissionList':trueList,
                                                 'mylen':mylen,
                                                 'aclen':aclen,
                                                 'acList':acList})

def rechargeMethod(request):
    usrname = request.session.get('usrname', '')
    try:
        nowUser = User.objects.get(usrname__exact=usrname)
    except:
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        if not 'payway' in request.POST:
            return HttpResponse('请选择一种充值方式!')
        money = int(request.POST['money_number'])
        if money <= 0:
            return HttpResponse('充值金额必须为正整数!')
        nowUser.money += money
        nowUser.save()
        return HttpResponseRedirect('/userCenter/')
    return HttpResponseRedirect('/userCenter/')