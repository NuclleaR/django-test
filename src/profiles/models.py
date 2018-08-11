from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')

        mail = self.normalize_email(email)
        user = self.model(email = mail)
        user.set_password(password)
        user.is_active = True
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password = None):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using = self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})


# class UserProfile(models.Model):
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, blank = False)
    name = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    img_url = models.URLField()
    date_joined = models.DateTimeField(default = timezone.now)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(
        _('staff status'),
        default = False,
        help_text = _('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default = True,
        help_text = _(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
