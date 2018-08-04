from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfile, ProfileFeedItem


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('created', 'modified',)}),
    )

    readonly_fields = (
        'created',
        'modified',
        'date_joined',
    )


admin.site.register(UserProfile, MyUserAdmin)
admin.site.register(ProfileFeedItem)
