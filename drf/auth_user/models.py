from django.db import models
from django.contrib.auth.models import AbstractUser

from auth_user.managers import UserManager


class AuthUser(AbstractUser):
    telegram_id = models.CharField(
        verbose_name='telegram_id',
        max_length=1000,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=100,
        blank=True, null=True,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='first_name',
        max_length=50,
        blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=50,
        blank=True, null=True
    )
    date_joined = models.DateTimeField(
        verbose_name='date_joined',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name='is_active',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='is_staff',
        default=False
    )
    is_verified = models.BooleanField(
        verbose_name='is_verified',
        default=False
    )

    object = UserManager()

    USERNAME_FIELD = 'telegram_id'

    class Meta(AbstractUser.Meta):
        verbose_name = 'auth_user'
        verbose_name_plural = 'auth_users'
        unique_together = ('telegram_id', 'username')

        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"{self.telegram_id}"