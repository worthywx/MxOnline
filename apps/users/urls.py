#coding=utf-8
__author__ = "worthy"
__date__ = '2017/11/7 20:45'
from django.conf.urls import url, include

from .views import UserinfoView, UploadImageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    #用户头像上传
    url(r'^image/upload$', UploadImageView.as_view(), name="image_upload"),
]