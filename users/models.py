from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Создание и сохранение пользователя с электронной почтой и паролем"""
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Создание и сохранение обычного пользователя"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание и сохранение модератора"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Модель, описывающая пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, verbose_name='имя', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name='город', null=True, blank=True)
    avatar = models.ImageField(verbose_name='фото', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

