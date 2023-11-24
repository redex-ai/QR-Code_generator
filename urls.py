from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('qr_code/', views.qr_code_view, name='qr_code'),
    # ... you can add other url patterns below ...
]