from django.urls import path, include

urlpatterns = [
    # ... your other url patterns here ...
    path('auth/', include('social_django.urls', namespace='social')),  # Social Auth URL
]
