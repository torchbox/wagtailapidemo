from django.db import models


class DeviceToken(models.Model):
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.token
