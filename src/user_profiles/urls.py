from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('auth', views.LoginViewSet, base_name = 'auth')
router.register('feed', views.ProfileFeedItemViewSet)
# router.register('example', views.ExampleView.as_view(), base_name = 'example')

urlpatterns = [
    path('', include(router.urls)),
    # path('example/', views.ExampleView.as_view(), name = 'example'),
]