from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Client(TimeStampModel):
    telegram_id = models.CharField(max_length=200)

    def __str__(self):
        return self.telegram_id