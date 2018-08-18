from django.db import models


# Abstract model to hold common information.
class BaseModel(models.Model):
    status = models.SmallIntegerField(choices=((1, 'NORMAL'), (0, 'DELETED'), (-1, 'UNKNOWN')), default=1)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
