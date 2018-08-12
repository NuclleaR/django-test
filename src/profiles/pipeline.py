from django.shortcuts import redirect
from .models import UserProfile


def redirect_if_no_refresh_token(backend, response, social, *args, **kwargs):
    if backend.name == 'google-oauth2' and social and \
            response.get('refresh_token') is None and \
            social.extra_data.get('refresh_token') is None:
        return redirect('/auth/login/google-oauth2?approval_prompt=force')


def create_social_user(backend, response, social, *args, **kwargs):
    # if 'domain' in response and response['domain'] == 'provectus.com':
    if 'is_new' in kwargs and kwargs['is_new']:
        details = dict(kwargs['details'])
        details['img_url'] = response['image']['url']
        details['gender'] = response['gender']
        email = details['email']
        del details['email']
        # details['cover'] = response['cover']
        user = UserProfile.objects.create_user(email = email, password = None, **details)
        return {'profile': user}
    # else:
    #     raise ValueError('User must have domain Provectus')
