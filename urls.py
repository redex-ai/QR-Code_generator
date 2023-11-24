from django.urls import path
from .views import qr_code_view

urlpatterns = [
    # ... your other url patterns ...
    path('generate_qr/', qr_code_view, name='generate_qr'),
    # ... your other url patterns ...
]
