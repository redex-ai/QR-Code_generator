from django.urls import path
from . import views

urlpatterns = [
    # ... your other url patterns here ...
    path('generate_qr/', views.generate_qr, name='generate_qr'),
]