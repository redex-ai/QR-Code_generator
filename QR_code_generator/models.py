from django.db import models


class GeneratedQRCode(models.Model):
    input_url = models.URLField(verbose_name='Input URL')
    qr_code_image = models.ImageField(upload_to='qr_codes/', verbose_name='QR Code Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'QR Code for {self.input_url}'
