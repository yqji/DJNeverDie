from django.contrib import admin

# Register your models here.
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'owner', 'content')
    search_fields = ('article', 'owner', 'content')
    list_filter = ('article', 'owner')


admin.site.register(Comment, CommentAdmin)
