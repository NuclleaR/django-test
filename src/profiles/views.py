from django.conf.global_settings import SESSION_COOKIE_NAME, SESSION_COOKIE_PATH, SESSION_COOKIE_DOMAIN
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from rest_framework import permissions, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# from . import permissions
from . import serializers
from . import models


class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('email', 'fullname', 'img_url')

    def list(self, request, *args, **kwargs):
        _list = super(ModelViewSet, self).list(request, *args, **kwargs)
        print(_list)
        return _list


class LogoutView(APIView):

    def get(self, request):
        print(request.COOKIES[SESSION_COOKIE_NAME])
        response = HttpResponseRedirect(redirect_to = '/')
        response.delete_cookie(
            SESSION_COOKIE_NAME,
            path = SESSION_COOKIE_PATH,
            domain = SESSION_COOKIE_DOMAIN,
        )
        return response


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

# class GoogleLogin(APIView):
#     pass
