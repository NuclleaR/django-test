from rest_framework.viewsets import ModelViewSet

from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileViewSet(ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
