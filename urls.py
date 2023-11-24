from django.urls import path
from . import views

urlpatterns = [
    # ... your other url patterns ...
    path('qr_code/', views.qr_code_view, name='qr_code'),
]