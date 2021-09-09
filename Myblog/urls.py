"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #用户注册与登陆
    path('user/',include('account.urls')),
    #博客文章
    path('',include('article.urls')),
    #图片墙
    path('album/',include('album.urls')),
    #留言版
    path('board/',include('interflow.urls')),
    #配置媒体资源的路由信息
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    #编辑器
    path('ckeditor/',include('ckeditor_uploader.urls')),
]
