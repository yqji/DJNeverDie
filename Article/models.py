from django.db import models
from django.contrib.auth.models import User

from Common.models import BaseModel
from Channel.models import Channel
from Tag.models import Tag


class Article(BaseModel):
    title = models.CharField('title', max_length=100)
    channel = models.ForeignKey(Channel, verbose_name='channel')
    author = models.ForeignKey(User, verbose_name='author')
    cover = models.CharField('cover path', max_length=100, default='')
    abstract = models.CharField('abstract', max_length=100)
    content = models.TextField('content', max_length=10000)
    views = models.IntegerField('view number', default=0)
    comments = models.IntegerField('comment number', default=0)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
