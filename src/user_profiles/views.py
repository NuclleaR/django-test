from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet, ViewSet

from .permissions import UpdateOwnProfilePermission
from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfilePermission,)
    filter_backends = (SearchFilter,)
    search_fields = ('email', 'username', 'first_name', 'last_name')


class LoginViewSet(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)
