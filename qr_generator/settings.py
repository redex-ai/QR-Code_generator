INSTALLED_APPS = [
    ...
    'social_django',
    ...
]

AUTHENTICATION_BACKENDS = [
    ...
    'social_core.backends.google.GoogleOAuth2',
    ...
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-oauth2-key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-oauth2-secret'

# Django settings
...
