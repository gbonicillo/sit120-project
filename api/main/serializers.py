from django.http import HttpResponseBadRequest
from rest_framework import serializers, pagination
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from textwrap import dedent

User = get_user_model()

# For retrieving user data used by nuxt $auth.user


class AuthUserSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "profile_picture",
            "type"
        ]

# For creating new users


class UserCreateSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "profile_picture",
            "type"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = make_password(validated_data.pop("password"))
        user = User(password=password, **validated_data)
        user.save()
        return user

# For updating user info


class UserUpdateSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "profile_picture"
        ]

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        # Put image upload here
        instance.save()
        return instance

# For updating user password


class UserPasswordSerializer (serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password"
        ]
