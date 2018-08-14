"""appfeedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.views import error_page
from . import settings
from profiles.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/logout/', LogoutView.as_view(), name = 'logout'),
    path('auth/error/', error_page, name = 'error'),
] + static(settings.MEDIA_URL)
