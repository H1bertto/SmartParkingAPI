from django.db import models


class Status(models.Model):
    name = models.CharField("Status", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '- Status'
        verbose_name_plural = '- Status'
