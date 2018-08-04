from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, LoginViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('auth', LoginViewSet, base_name = 'auth')

urlpatterns = [
    path('', include(router.urls)),
]