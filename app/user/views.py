"""
Views for the User API
"""
from rest_framework import generics, status
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import (
    UserSerializer,
    AuthTokenSerializer
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in this system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES