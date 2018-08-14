import six
from social_django.middleware import SocialAuthExceptionMiddleware


class AuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        strategy = getattr(request, 'social_strategy', None)
        return '%s. You should login with %s' % \
               (six.text_type(exception), ', '.join(strategy.setting('WHITELISTED_DOMAINS')))

    def get_redirect_uri(self, request, exception):
        strategy = getattr(request, 'social_strategy', None)
        # return strategy.setting('LOGIN_ERROR_URL')
        return '/auth/error/'
