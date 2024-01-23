import random

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import User


class AuthTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(label=_("Phone Number"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        if not phone_number or not password:
            raise serializers.ValidationError(
                _('Must include "phone_number" and "password".'), code="authorization"
            )

        user = authenticate(
            request=self.context.get("request"),
            phone_number=phone_number,
            password=password,
        )

        if user:
            if not user.is_active:
                raise serializers.ValidationError(
                    _("User account is not active."), code="authorization"
                )
        else:
            raise serializers.ValidationError(
                _("Unable to log in with provided credentials."), code="authorization"
            )

        attrs["user"] = user
        return attrs


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number"]

    def create(self, validated_data):
        user = User(
            phone_number=validated_data["phone_number"],
            is_active=False,  # Foydalanuvchini dastlabki holatda faol emas deb belgilash
            otp_code=str(random.randint(100000, 999999)),
        )

        user.save()
        try:
            pass
        except Exception as e:
            # Xatolikni qayd etish va kerak bo'lsa boshqa choralar ko'rish
            print(f"SMS sending failed: {e}")

        return user


class AccountVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField(max_length=6)

    def validate(self, data):
        user = User.objects.filter(phone_number=data["phone_number"]).first()
        if user is None:
            raise serializers.ValidationError(
                "User with this phone number does not exist."
            )
        if user.verification_code != data["verification_code"]:
            raise serializers.ValidationError("Verification code is incorrect.")

        user.is_active = True  # Foydalanuvchini faol deb belgilash
        user.save()
        return {"user": user}


class SetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get("phone_number")
        otp_code = data.get("otp_code")

        try:
            user = User.objects.get(phone_number=phone_number, otp_code=otp_code)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "Invalid phone number or verification code."
            )

        # Here, you can add any additional validation logic if needed
        # For example, you might want to check if the verification code is expired

        return data
