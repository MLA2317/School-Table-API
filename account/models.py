from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('User should have a username')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError('User should have a password')

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=220, unique=True, verbose_name='Username', db_index=True)
    bio = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='profile/', null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Modified Date')

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
