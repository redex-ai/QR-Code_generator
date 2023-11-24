from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('generate_qr/', views.qr_code_view, name='generate_qr'),
    # ... other url patterns ...
]
