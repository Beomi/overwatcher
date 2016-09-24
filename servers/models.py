from django.db import models
from core.models import TimeStampModel


class ServerInfo(TimeStampModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ServerNowStatus(TimeStampModel):
    server = models.ForeignKey('ServerInfo')
    status = models.ForeignKey('ServerStatus')

    def __str__(self):
        return self.server.name + self.status.status


class ServerStatus(TimeStampModel):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status
