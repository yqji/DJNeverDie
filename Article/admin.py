from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'channel', 'views', 'comments')
    search_fields = ('title', 'author', 'channel')
    list_filter = ('channel', 'status')


admin.site.register(Article, ArticleAdmin)
