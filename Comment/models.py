from django.db import models

from Article.models import Article
from Common.models import BaseModel


class Comment(BaseModel):
    article = models.ForeignKey(Article, verbose_name='article')
    owner = models.CharField('comment publisher', max_length=100, default='Anonym')
    to_comment_id = models.IntegerField('to comment id', default=0)
    content = models.TextField('content', max_length=10000)

    @property
    def to_comment(self):
        if not self.to_comment_id:
            return None
        else:
            return Comment.objects.get(id=self.to_comment_id)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content[:15]
