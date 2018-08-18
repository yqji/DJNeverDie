from django.shortcuts import render_to_response
# from django.template import RequestContext

from .models import Channel


def get_channels(request):
    channels = Channel.objects.all().order_by('id')
    return render_to_response('djnd_index.html',
                              {'channels': channels, })
