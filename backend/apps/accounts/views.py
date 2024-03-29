# api/auth.py
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .auth_serializers import (AccountVerificationSerializer,
                               AuthTokenSerializer, RegistrationSerializer,
                               SetPasswordSerializer)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "phone_number": user.phone_number,
                # "address": user.address if user.image else None,
                "address": user.address,
            }
        )
