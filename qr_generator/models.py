from django.db import models


class QRCode(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
