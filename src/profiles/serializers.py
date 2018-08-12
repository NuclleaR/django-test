from rest_framework import serializers
from django.contrib.auth.models import Group
from profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()

    class Meta:
        model = UserProfile
        fields = (
            'email',
            'username',
            'fullname',
            # 'first_name',
            # 'last_name',
            'img_url',
        )
        read_only_fields = (
            'email',
            'username',
            'fullname',
            # 'first_name',
            # 'last_name',
            'img_url',
        )

    # def create(self, validated_data):
    #     user = UserProfile(
    #         email = validated_data['email'],
    #     )
    #     # user.set_password(validated_data['password'])
    #     user.save()
    #     return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )
