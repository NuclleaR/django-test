from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

# from . import permissions
from . import serializers
from . import models


class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    # filter_backends = (SearchFilter,)
    # search_fields = ('email', 'name', 'first_name', 'last_name', 'img_url')


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

# class GoogleLogin(APIView):
#     pass
