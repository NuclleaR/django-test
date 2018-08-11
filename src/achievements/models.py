import uuid
from django.db import models

from profiles.models import UserProfile


class Achievement(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    object_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    image_url = models.ImageField(upload_to = 'media/', default = None, blank = True)
    description = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class AchievementUser(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    achievement = models.ForeignKey(Achievement, to_field = 'object_id', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
