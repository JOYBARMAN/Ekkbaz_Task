"""Serializers for business"""

from rest_framework import serializers

from business.models import Business
from core.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "uid",
            "username",
            "email",
        ]


class BusinessBaseSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
        model = Business
        fields = [
            "id",
            "uid",
            "user",
            "business_name",
            "latitude",
            "longitude",
            "status",
        ]
        read_only_fields = [
            "id",
            "uid",
        ]


class BusinessListSerializer(BusinessBaseSerializer):
    class Meta(BusinessBaseSerializer.Meta):
        fields = BusinessBaseSerializer.Meta.fields + [
            "created_at",
            "updated_at",
        ]
        read_only_fields = BusinessBaseSerializer.Meta.read_only_fields + [
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        validated_data["user"] = self.context.get("user")
        business_instance = Business.objects.create(**validated_data)

        # Serialize the created instance before returning it
        serialized_instance = self.__class__(
            business_instance, context=self.context
        ).data
        return serialized_instance
