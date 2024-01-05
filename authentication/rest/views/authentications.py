"""Views for authentication"""

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from authentication.rest.serializers.authentications import (
    RegistrationSerializer,
    LoginSerializer,
    ActivateAccountSerializer,
    ChangePasswordSerializer,
    PasswordResetMailSerializer,
    PasswordResetSerializer,
)

from core.permissions import AllowAny, IsAuthenticated


class RegistrationView(CreateAPIView):
    """User registration view"""

    serializer_class = RegistrationSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView):
    """User login view"""

    serializer_class = LoginSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class ActiveAccountView(CreateAPIView):
    """User active account view"""

    serializer_class = ActivateAccountSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class ChangePasswordView(CreateAPIView):
    """User change password view"""

    serializer_class = ChangePasswordSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class PasswordResetMailView(CreateAPIView):
    """User forgot password view"""

    serializer_class = PasswordResetMailSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class PasswordResetView(CreateAPIView):
    """User password reset view"""

    serializer_class = PasswordResetSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"uid": kwargs.get("uid"), "token": kwargs.get("token")},
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)
