from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'is_active',
            'user_image'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileFeedItem
        fields = (
            'id',
            'user_profile',
            'status_text',
            'date_created'
        )
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }
