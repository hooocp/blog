from django.contrib import admin
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    field = ['title', 'desc', 'content', 'tag']


# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
