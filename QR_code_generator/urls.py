from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns...

    # Add a new URL pattern for the QR code generation view
    path('generate_qr/', views.generate_qr, name='generate_qr'),
]