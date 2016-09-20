from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ServerInfo(TimeStampModel):
    name = models.CharField(max_length=10)


class ServerNowStatus(TimeStampModel):
    server = models.ForeignKey('ServerInfo')
    status = models.ForeignKey('ServerStatus')


class ServerStatus(TimeStampModel):
    status = models.CharField(max_length=4)