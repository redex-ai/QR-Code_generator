from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    # ... other url patterns ...
]