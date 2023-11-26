from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('url', 'timestamp', 'qr_code_image')
    list_filter = ('timestamp',)
    search_fields = ('url',)
