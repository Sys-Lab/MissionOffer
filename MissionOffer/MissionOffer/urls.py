"""MissionOffer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Login
    url(r'^$','Login.views.toIndexMethod',name=''),
    url(r'^register/$','Login.views.registerMethod',name='register'),
    url(r'^login/$','Login.views.loginMethod',name='login'),
    url(r'^index/$','Login.views.indexMethod',name='index'),
    # url(r'^index/(?P<type>\w*)/*(?P<status>\w*)/*$','Login.views.indexMethod',name='index'),
    url(r'^logout/$','Login.views.logoutMethod',name='logout'),
    url(r'^userCenter/$','Login.views.userCenterMethod',name='userCenter'),
    url(r'^loginCheck/$','Login.views.loginCheckMethod',name='loginCheck'),
    url(r'^register/activate/(?P<authKey>\w+)/$','Login.views.activateMethod',name='activate'),

    # OfferMission
    url(r'^offer/$','OfferMission.views.offerMethod',name='offer'),
    # url(r'^uploadFile/$','OfferMission.views.uploadFileMethod',name='uploadFileMethod'),
    url(r'^downloadFile/(?P<attachmentID>\d+)/$','OfferMission.views.downloadFileMethod',name='downloadFile'),

    # ViewMission
    url(r'^mission/(?P<missionID>\d+)/$','OfferMission.views.viewMissionMethod',name='viewMission'),

    # statics
    url(r'^statics/(?P<path>.*)', 'django.views.static.serve',{'document_root':settings.STATIC_PATH}),
]
