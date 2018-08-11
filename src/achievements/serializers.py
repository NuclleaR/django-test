from rest_framework import serializers
from .models import Achievement


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = (
            'id',
            'name',
            'object_id',
            'image_url',
            'description',
        )
