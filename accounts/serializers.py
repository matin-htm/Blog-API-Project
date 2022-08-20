from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter

from phonenumber_field.serializerfields import PhoneNumberField


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = [
            "id",
            "is_superuser",
            "first_name",
            "last_name",
            "phone_number",
            "bio",
            "age",
            "date_joined",
        ]
        fields = [
            "id",
            "is_superuser",
            "first_name",
            "last_name",
            "phone_number",
            "bio",
            "age",
            "date_joined",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "is_superuser",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "date_joined",
            "last_login",
            "bio",
            "age",
        ]
        read_only_fields = [
            "is_superuser",
            "password",
        ]


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = PhoneNumberField()

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
        ]

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.save()
        adapter.save_user(request, user, self)
        return user
