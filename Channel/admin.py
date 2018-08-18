from django.contrib import admin

# Register your models here.
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Channel, ChannelAdmin)
