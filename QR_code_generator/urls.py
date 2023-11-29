from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('generate/', views.generate_qr, name='generate_qr'),
    # ... you can add other url patterns here ...
]