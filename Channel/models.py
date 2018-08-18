from django.db import models
from Common.models import BaseModel


class Channel(BaseModel):
    name = models.CharField('channel name', max_length=100)
    desc = models.CharField('channel description', max_length=10000)
    img = models.CharField('channel image source', max_length=10000, default='')
    article_num = models.BigIntegerField('article counts', default=0)

    @property
    def cover(self):
        # TODO
        pass

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

    def __str__(self):
        return self.name
