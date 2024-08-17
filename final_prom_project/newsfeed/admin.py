from django.contrib import admin
from .models import News, User
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'author']


admin.site.register(News, NewsAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'birthday', 'email', 'about']


admin.site.register(User, UserAdmin)
