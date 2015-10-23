from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from Login.forms import *
from Login.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

def loginCheckMethod(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        uf = LoginForm(request.POST)
        if uf.is_valid():
            un = uf.cleaned_data['UN']
            pw = uf.cleaned_data['PW']
            nowUser = User.objects.filter(usrname__exact=un, password__exact=pw)
            if nowUser:  # 登录成功
                request.session['usrname'] = un
                return HttpResponseRedirect('/index')
            else:  # 先在终端输出错误，之后再编写在网页上提示错误的功能
                print('用户名或密码错误')
                return HttpResponse()

def loginMethod(request):
    return render_to_response('login.html', {})

def createNewUser(post):
    newUser = User()  # 创建新用户，加入到数据库中。
    newUser.usrname = post['usrname']
    newUser.password = post['password']
    newUser.sex = post['sex']
    newUser.edu = post['edu']
    newUser.realname = post['realname']
    newUser.idNumber = post['idNumber']
    newUser.email = post['email']
    newUser.phonenumber = post['phonenumber']
    newUser.eval = post['eval']
    newUser.save()
    send_mail('MissionOffer register e-mail', 'This is a test e-mail from MissionOffer website.', 'missionoffer@sina.com',    [newUser.email], fail_silently=False)
    return newUser


def registerMethod(request):
    if request.method == 'POST':
        if 'submit' in request.POST:  # 先在终端输出错误，之后再编写在网页上提示错误的功能
            if len(request.POST['usrname']) <= 0:  # 没输入用户名
                print('请输入用户名！')
                return render_to_response('registerframework.html', {})
            if len(request.POST['password']) <= 0:  # 没输入密码
                print('请输入密码！')
                return render_to_response('registerframework.html', {})
            if len(request.POST['email']) <= 0:  # 没输入邮箱
                print('请输入邮箱！')
                return render_to_response('registerframework.html', {})
            if request.POST['password'] != request.POST['password']:  # 密码不一致
                print('密码不一致')
                return render_to_response('registerframework.html', {})
            findList = User.objects.filter(usrname=request.POST['usrname'])
            if len(findList) > 0:  # 用户已存在
                print('用户已存在')
                return render_to_response('registerframework.html', {})
            findList = User.objects.filter(email=request.POST['email'])
            if len(findList) > 0:  # 邮箱已存在
                print('邮箱已存在')
                return render_to_response('registerframework.html', {})

            createNewUser(request.POST)
            request.session['usrname'] = request.POST['usrname']
            return HttpResponseRedirect('/index')
            # return render_to_response('afterregisterframework.html',request.POST)
    return render_to_response('registerframework.html', {})

def indexMethod(request):
    usrname = request.session.get('usrname', '')
    return render_to_response('framework.html',{'usrname': usrname})

def logoutMethod(requset):
    del requset.session['usrname']
    return HttpResponseRedirect('/index')

def userCenterMethod(request):
    usrname = request.session.get('usrname', '')
    return render_to_response('userCenter.html',{'usrname':usrname})