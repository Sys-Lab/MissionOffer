from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse


def loginMethod(request):
    if request.method == 'POST':
        return render_to_response('afterLogin.html', request.POST)
    return render_to_response('login framework.html', {})


def registerMethod(request):
    if request.method == 'POST':
        return render_to_response('afterLogin.html', request.POST)
    return render_to_response('register framework.html', {})
