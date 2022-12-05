from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from ..managers import CustomUserManager
from .choise import CustomUserRoleChoice


class AbstractTimeTracker(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('utils.tracker_model.created_at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('utils.tracker_model.updated_at')
    )

    class Meta:
        abstract = True
        ordering = ('updated_at', 'created_at')


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractTimeTracker):
    name = models.CharField(_('username'), max_length=255, blank=True)
    surname = models.CharField(_('username'), max_length=255, blank=True)
    phone = models.CharField(_('phone number'), max_length=30, unique=True)
    role = models.CharField(
        max_length=100,
        choices=CustomUserRoleChoice.choices,
        default=CustomUserRoleChoice.DEFAULT.value,
        verbose_name='Role'
    )
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified = models.BooleanField(_('verified'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-updated_at', '-created_at']

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = CustomUserRoleChoice.SUPER_ADMIN.value

        return super(CustomUser, self).save(*args, **kwargs)