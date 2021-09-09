from django.contrib import admin
from .models import *

admin.site.site_title = '博客管理后台'

admin.site.site_header = '博客管理'
@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'tag',
        'user',
    ]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_id=request.user.id)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field == 'user':
            id = request.user.id
            kwargs['queryset'] = MyUser.objects.filter(id=id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
        'content',
        'articlephoto',
        'created',
        'upload',
    ]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author_id=request.user.id)
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field =='article_tag':
            id =request.user.id
            kwargs['queryset'] = ArticleTag.objects.filter(user_id=id)
        return super().formfield_for_manytomany(db_field,request,**kwargs)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            id = request.user.id
            kwargs['queryset'] = MyUser.objects.filter(id=id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'article',
        'commentator',
        'content',
        'created',
    ]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(article__author__id=request.user.id)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field == 'article':
            id = request.user.id
            kwargs['queryset'] = Comment.objects.filter(article__author__id=id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
# Register your models here.
