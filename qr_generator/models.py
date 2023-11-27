from django.db import models


class GeneratedQRCode(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/', verbose_name='QR Code Image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}'
