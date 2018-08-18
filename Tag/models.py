from django.db import models

from Common.models import BaseModel


class Tag(BaseModel):
    name = models.CharField('name', max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
