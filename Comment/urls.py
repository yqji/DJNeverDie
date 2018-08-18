from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^list/(?P<channel_name>.+)', get_comments, name='comments')
]
