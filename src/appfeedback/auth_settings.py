# SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'

# SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
# SOCIAL_AUTH_STORAGE = 'profiles.models.CustomDjangoStorage'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# RAISE_EXCEPTIONS = True

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'access_type': 'offline',
    'approval_prompt': 'auto'
}

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/api/profile/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    # 'social_core.pipeline.social_auth.mail_validation',
    'social_core.pipeline.social_auth.social_user',
    'profiles.pipeline.redirect_if_no_refresh_token',
    'social_core.pipeline.user.get_username',
    # 'social_core.pipeline.social_auth.associate_by_email',
    'profiles.pipeline.create_social_user',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)