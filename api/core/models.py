import jwt
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

import datetime


class ClientManager(BaseUserManager):
    def create_user(self, username, email, first_name, second_name, third_name, birth_date, phone, password=None):
        if username is None:
            raise TypeError('User must have a username.')
        if email is None:
            raise TypeError('User must have an email address.')
        if first_name is None:
            raise TypeError('User must have an first name.')
        if second_name is None:
            raise TypeError('User must have an second name.')
        if third_name is None:
            raise TypeError('User must have an third name.')

        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name,
                          second_name=second_name, third_name=third_name, birth_date=birth_date, phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, second_name, third_name, birth_date, phone, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, first_name, second_name, third_name, birth_date, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Police(models.Model):
    geoJson = models.TextField(blank=False, null=False)
    cadastralNumber = models.CharField(max_length=50, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    term = models.IntegerField(blank=False, null=False)
    coating = models.FloatField(blank=False, null=False)
    startDate = models.DateField(blank=False, null=False)
    docType = models.CharField(blank=False, null=False, max_length=20)
    docId = models.IntegerField(blank=False, null=False)
    status = models.IntegerField(blank=False, null=False)
    ndvi = ArrayField(
        models.FloatField(blank=False, null=False), default=[]
    )
    dates = ArrayField(
        models.DateField(blank=False, null=False), default=[]
    )

    class Meta:
        db_table = 'Police'


class Notification(models.Model):
    created = models.DateField(blank=False, null=False, auto_now_add=True)
    notes = models.CharField(blank=False, null=False, max_length=200)
    state = models.CharField(blank=False, null=False, max_length=10, default='unread')


class Client(AbstractBaseUser, PermissionsMixin):
    polices = models.ManyToManyField(Police, null=True)
    username = models.CharField(max_length=200, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    second_name = models.CharField(max_length=100, blank=False, null=False)
    third_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True),
    notifications = models.ManyToManyField(Notification, null=True, default=[])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = ClientManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class ForeignPassport(models.Model):
    passport_issue = models.DateField(blank=True, null=True)
    series_and_number = models.CharField(max_length=20, blank=True, null=True)
    client = models.ForeignKey(Client, unique=True, blank=False, null=False, on_delete=models.CASCADE)


class IDCard(models.Model):
    passport_issue = models.DateField(blank=True, null=True)
    issued_by = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    notation = models.CharField(max_length=20, blank=True, null=True)
    client = models.ForeignKey(Client, unique=True, blank=False, null=False, on_delete=models.CASCADE)


class UkrainePassport(models.Model):
    series_and_number = models.CharField(max_length=20, blank=False, null=False)
    passport_issue = models.DateField(blank=True, null=True)
    issued_by = models.CharField(blank=False, null=False, max_length=20)
    client = models.ForeignKey(Client, unique=True, blank=False, null=False, on_delete=models.CASCADE)
