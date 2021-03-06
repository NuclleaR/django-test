from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email, password = None):
        if not username:
            raise ValueError('User must have username')
        if not email:
            raise ValueError('User must have email')

        email = self.normalize_email(email)
        user = self.model(email = email, username = username)
        user.set_password(password)

        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, password = None):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using = self._db)
        return user


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatars/user_<id>/<filename>
    print('>>> instance.id: ', instance.id)
    return 'media/avatars/user_{0}/{1}'.format(instance.id, filename)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    username = models.CharField(max_length = 255, unique = True)
    first_name = models.CharField(verbose_name = 'first name', max_length = 30, blank = True)
    last_name = models.CharField(verbose_name = 'last name', max_length = 150, blank = True)
    is_active = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    user_image = models.ImageField(upload_to = user_directory_path, default = None, blank = True)
    date_joined = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True, blank = True)
    modified = models.DateTimeField(auto_now = True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'email'
    ]

    def get_fullname(self):
        """Returns full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name).strip()

    def __str__(self):
        if not self.get_fullname():
            return self.username
        else:
            return self.get_fullname()


class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.status_text

