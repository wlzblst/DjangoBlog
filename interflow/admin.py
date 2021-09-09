from django.contrib import admin
from .models import Board
from account.models import MyUser
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'content',
        'created',
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
# Register your models here.
