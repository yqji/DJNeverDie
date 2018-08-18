from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^list/(?P<channel_name>.+)', get_articles, name='articles'),
    url(r'^detail/(?P<article_id>\d+)', get_article, name='article'),
    url(r'^create/$', create_article, name='create_article')
]
